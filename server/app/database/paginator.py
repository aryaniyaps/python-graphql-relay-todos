from collections.abc import Sequence
from dataclasses import dataclass
from typing import Generic, TypeVar
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import InstrumentedAttribute
from sqlalchemy.sql import Select

from app.lib.constants import DEFAULT_PAGINATION_LIMIT

from .base import Base

ModelType = TypeVar("ModelType", bound=Base)

CursorType = TypeVar("CursorType", UUID, str)


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
    def __validate_pagination_arguments(
        first: int | None,
        last: int | None,
        before: CursorType | None,
        after: CursorType | None,
    ) -> None:
        """Validate the given pagination arguments."""
        if first and last:
            raise ValueError("Cannot provide both `first` and `last`")
        if first and before:
            raise ValueError("`first` cannot be provided with `before`")
        if last and after:
            raise ValueError("`last` cannot be provided with `after`")

    async def paginate(
        self,
        statement: Select[tuple[ModelType]],
        last: int | None = None,
        first: int | None = None,
        before: CursorType | None = None,
        after: CursorType | None = None,
    ) -> PaginatedResult[ModelType, CursorType]:
        """Paginate the given SQLAlchemy statement."""
        self.__validate_pagination_arguments(
            first=first,
            last=last,
            after=after,
            before=before,
        )

        limit = first or last

        if limit is None:
            # set default pagination limit
            limit = DEFAULT_PAGINATION_LIMIT

        # TODO: make sure IDs are time sortable
        # Cursors should NOT be UUIDs

        if before is not None:
            query = statement.where(self._paginate_by < before)
        elif after is not None:
            query = statement.where(self._paginate_by > after)

        query = query.limit(limit + 1)

        scalars = await self._session.scalars(query)

        results = scalars.all()

        if first is not None:
            entities = results[:first]
        elif last is not None:
            entities = results[-last:]

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
