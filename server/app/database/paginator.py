from collections.abc import Sequence
from dataclasses import dataclass
from typing import Generic, TypeVar
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import InstrumentedAttribute
from sqlalchemy.sql import Select

from .base import Base

CursorType = TypeVar("CursorType", UUID, str)
ModelType = TypeVar("ModelType", bound=Base)


@dataclass
class PageInfo(Generic[CursorType]):
    has_next_page: bool
    start_cursor: CursorType | None


@dataclass
class PaginatedResult(Generic[ModelType, CursorType]):
    entities: Sequence[ModelType]
    page_info: PageInfo[CursorType]


class Paginator(Generic[ModelType, CursorType]):
    def __init__(
        self,
        session: AsyncSession,
        model: type[ModelType],
        paginate_by: InstrumentedAttribute[CursorType],
    ) -> None:
        self._session = session
        self._paginate_by = paginate_by or inspect(model).mapper.primary_key[0]

    async def paginate(
        self,
        statement: Select[tuple[ModelType]],
        limit: int,
        cursor: CursorType | None = None,
    ) -> PaginatedResult[ModelType, CursorType]:
        query = statement.order_by(self._paginate_by)

        if cursor is not None:
            query = query.where(self._paginate_by > cursor)

        query = query.limit(limit + 1)

        scalars = await self._session.scalars(query)

        results = scalars.all()

        has_next_page = len(results) > limit
        entities = results[:limit]
        start_cursor = (
            getattr(entities[0], self._paginate_by.name) if entities else None
        )

        return PaginatedResult(
            entities=entities,
            page_info=PageInfo(
                has_next_page=has_next_page,
                start_cursor=start_cursor,
            ),
        )
