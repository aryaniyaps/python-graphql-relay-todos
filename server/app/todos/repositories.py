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

    async def get(self, todo_id: int) -> Todo | None:
        """Get todo by ID."""
        return await self._session.scalar(
            select(Todo).where(
                Todo.id == todo_id,
            ),
        )

    async def get_many_by_ids(self, todo_ids: list[int]) -> list[Todo | None]:
        """Get multiple todos by IDs."""
        stmt = select(Todo).where(Todo.id.in_(todo_ids))
        todo_by_id = {todo.id: todo for todo in await self._session.scalars(stmt)}

        return [todo_by_id.get(todo_id) for todo_id in todo_ids]

    async def get_all(
        self,
        first: int | None = None,
        last: int | None = None,
        before: int | None = None,
        after: int | None = None,
    ) -> PaginatedResult[Todo, int]:
        """Get a paginated result of todos."""
        paginator: Paginator[Todo, int] = Paginator(
            session=self._session,
            paginate_by=Todo.id,
            reverse=True,
        )

        return await paginator.paginate(
            statement=select(Todo),
            first=first,
            last=last,
            before=before,
            after=after,
        )

    async def delete(self, todo_id: int) -> None:
        """Delete a todo by ID."""
        await self._session.execute(
            delete(Todo).where(
                Todo.id == todo_id,
            ),
        )
        await self._session.commit()
