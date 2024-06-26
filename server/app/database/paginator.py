from collections.abc import Sequence
from dataclasses import dataclass
from typing import Generic, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import InstrumentedAttribute
from sqlalchemy.sql import Select

from app.lib.constants import DEFAULT_PAGINATION_LIMIT

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
    ) -> None:
        """Validate the given pagination arguments."""
        if first and last:
            first_and_last_error = "Cannot provide both `first` and `last`"
            raise ValueError(first_and_last_error)
        if first and before:
            first_and_before_error = "`first` cannot be provided with `before`"
            raise ValueError(first_and_before_error)
        if last and after:
            last_and_after_error = "`last` cannot be provided with `after`"
            raise ValueError(last_and_after_error)

    async def paginate(
        self,
        statement: Select[tuple[ModelType]],
        last: int | None = None,
        first: int | None = None,
        before: CursorType | None = None,
        after: CursorType | None = None,
    ) -> PaginatedResult[ModelType, CursorType]:
        """Paginate the given SQLAlchemy statement."""
        self.__validate_arguments(
            first=first,
            last=last,
            after=after,
            before=before,
        )

        limit = first or last or DEFAULT_PAGINATION_LIMIT

        if before is not None:
            statement = statement.where(self._paginate_by < before)
        elif after is not None:
            statement = statement.where(self._paginate_by > after)

        statement = statement.limit(limit + 1)

        scalars = await self._session.scalars(statement)

        results = scalars.all()

        entities = results[-limit:] if before is not None else results[:limit]

        if before is not None:
            has_next_page = True
            has_previous_page = len(results) > limit
        else:
            # we are paginating forwards by default
            has_next_page = len(results) > limit
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
