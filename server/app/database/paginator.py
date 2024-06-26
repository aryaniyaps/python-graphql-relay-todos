from collections.abc import Sequence
from dataclasses import dataclass
from typing import Generic, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import InstrumentedAttribute
from sqlalchemy.sql import Select

from app.lib.constants import MAX_PAGINATION_LIMIT

from .base import Base

ModelType = TypeVar("ModelType", bound=Base)

CursorType = TypeVar("CursorType", int, str)


@dataclass
class PageInfo(Generic[CursorType]):
    has_next_page: bool
    has_previous_page: bool
    start_cursor: CursorType | None
    end_cursor: CursorType | None


@dataclass
class PaginatedResult(Generic[ModelType, CursorType]):
    entities: Sequence[ModelType]
    page_info: PageInfo[CursorType]


class Paginator(Generic[ModelType, CursorType]):
    def __init__(
        self,
        session: AsyncSession,
        paginate_by: InstrumentedAttribute[CursorType],
    ) -> None:
        self._session = session
        self._paginate_by: InstrumentedAttribute[CursorType] = paginate_by

    @staticmethod
    def __validate_arguments(
        first: int | None,
        last: int | None,
        before: CursorType | None,
        after: CursorType | None,
    ) -> int:
        """
        Validate the given pagination arguments.

        Returns the pagination limit specified.
        """
        # FIXME: relay spec doesn't specify the commented out checks, it was there in dummy
        # strawberry docs code
        if first is not None and last is not None:
            first_and_last_error = "Cannot provide both `first` and `last`"
            raise ValueError(first_and_last_error)

        if first is not None:
            if first < 0:
                first_not_positive_error = "`first` must be a positive integer"
                raise ValueError(first_not_positive_error)
            if first > MAX_PAGINATION_LIMIT:
                max_pagination_limit_error = f"`first` exceeds pagination limit of {MAX_PAGINATION_LIMIT} records"
                raise ValueError(max_pagination_limit_error)
            # if before is not None:
            #     first_and_before_error = "`first` cannot be provided with `before`"
            #     raise ValueError(first_and_before_error)
            return first

        if last is not None:
            if last < 0:
                last_not_positive_error = "`last` must be a positive integer"
                raise ValueError(last_not_positive_error)
            if last > MAX_PAGINATION_LIMIT:
                max_pagination_limit_error = (
                    f"`last` exceeds pagination limit of {MAX_PAGINATION_LIMIT} records"
                )
                raise ValueError(max_pagination_limit_error)
            # if after is not None:
            #     last_and_after_error = "`last` cannot be provided with `after`"
            #     raise ValueError(last_and_after_error)
            return last

        no_first_and_last_error = (
            "You must provide either `first` or `last` to paginate"
        )
        raise ValueError(no_first_and_last_error)

    async def paginate(
        self,
        statement: Select[tuple[ModelType]],
        last: int | None = None,
        first: int | None = None,
        before: CursorType | None = None,
        after: CursorType | None = None,
    ) -> PaginatedResult[ModelType, CursorType]:
        """Paginate the given SQLAlchemy statement."""
        pagination_limit = self.__validate_arguments(
            first=first,
            last=last,
            after=after,
            before=before,
        )

        if after is not None:
            print("AFTER VALUE: ", after)
            statement = statement.where(self._paginate_by > after)
        elif before is not None:
            statement = statement.where(self._paginate_by < before)

        statement = statement.limit(pagination_limit + 1)

        print("PAGINATION LIMIT VALUE: ", pagination_limit)

        scalars = await self._session.scalars(statement)

        results = scalars.all()

        print("RESULTS: ", [todo.id for todo in results])

        # TODO: check this!!
        # should it be:
        # entities = (
        #     results[-pagination_limit:]
        #     if last is not None
        #     else results[:pagination_limit]
        # )
        entities = (
            results[-pagination_limit:]
            if last is not None
            else results[:pagination_limit]
        )

        if before is not None:
            has_next_page = True
            has_previous_page = len(results) > pagination_limit
        else:
            # we are paginating forwards by default
            has_next_page = len(results) > pagination_limit
            has_previous_page = after is not None

        start_cursor = (
            getattr(
                entities[0],
                self._paginate_by.name,
            )
            if entities
            else None
        )

        end_cursor = (
            getattr(
                entities[-1],
                self._paginate_by.name,
            )
            if entities
            else None
        )

        return PaginatedResult(
            entities=entities,
            page_info=PageInfo(
                has_next_page=has_next_page,
                has_previous_page=has_previous_page,
                start_cursor=start_cursor,
                end_cursor=end_cursor,
            ),
        )
