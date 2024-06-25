from uuid import UUID

from sqlalchemy import delete, desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.paginator import PaginatedResult, Paginator

from .models import Todo


class TodoRepo:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, content: str) -> Todo:
        """Create a new todo."""
        todo = Todo(content=content)
        self._session.add(todo)
        await self._session.commit()
        return todo

    async def get(self, todo_id: str) -> Todo | None:
        """Get todo by ID."""
        return await self._session.scalar(
            select(Todo).where(
                Todo.id == todo_id,
            ),
        )

    async def get_all(
        self,
        limit: int,
        cursor: UUID | None = None,
    ) -> PaginatedResult[Todo, UUID]:
        """Get all todos."""
        paginator = Paginator(
            session=self._session,
            model=Todo,
            paginate_by=Todo.id,
        )

        return await paginator.paginate(
            statement=select(Todo).order_by(
                desc(Todo.created_at),
            ),
            limit=limit,
            cursor=cursor,
        )

    async def delete(self, todo_id: str) -> None:
        """Delete a todo by ID."""
        await self._session.execute(
            delete(Todo).where(
                Todo.id == todo_id,
            ),
        )
        await self._session.commit()
