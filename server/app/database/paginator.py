from collections.abc import Sequence
from dataclasses import dataclass
from datetime import datetime
from typing import Generic, TypeVar
from uuid import UUID

from sqlalchemy import desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import InstrumentedAttribute
from sqlalchemy.sql import Select

from .base import Base

CursorType = TypeVar("CursorType", UUID, str)
ModelType = TypeVar("ModelType", bound=Base)


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
        paginate_order_by: InstrumentedAttribute[datetime],
    ) -> None:
        self._session = session
        self._paginate_by: InstrumentedAttribute[CursorType] = paginate_by
        self._paginate_order_by = paginate_order_by

    async def paginate(
        self,
        statement: Select[tuple[ModelType]],
        limit: int,
        before: CursorType | None = None,
        after: CursorType | None = None,
    ) -> PaginatedResult[ModelType, CursorType]:
        if before is not None and after is not None:
            invalid_arguments_error = (
                "Only one of 'before' and 'after' can be specified"
            )
            raise ValueError(invalid_arguments_error)

        query = statement.order_by(
            self._paginate_order_by
            if before is not None
            else desc(self._paginate_order_by)
        )

        if before is not None:
            query = query.where(self._paginate_by < before)
        elif after is not None:
            query = query.where(self._paginate_by > after)

        query = query.limit(limit + 1)

        scalars = await self._session.scalars(query)

        results = scalars.all()

        has_next_page = after is not None and len(results) > limit
        has_previous_page = before is not None and len(results) > 0
        entities = results[:limit]
        start_cursor = (
            getattr(entities[0], self._paginate_by.name) if entities else None
        )
        end_cursor = getattr(entities[-1], self._paginate_by.name) if entities else None

        return PaginatedResult(
            entities=entities,
            page_info=PageInfo(
                has_next_page=has_next_page,
                has_previous_page=has_previous_page,
                start_cursor=start_cursor,
                end_cursor=end_cursor,
            ),
        )
