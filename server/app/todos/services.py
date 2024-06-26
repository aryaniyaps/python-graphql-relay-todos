from app.database.paginator import PaginatedResult

from .models import Todo
from .repositories import TodoRepo


class TodoService:
    def __init__(self, todo_repo: TodoRepo) -> None:
        self._todo_repo = todo_repo

    async def create_todo(self, content: str) -> Todo:
        """Create a new todo."""
        return await self._todo_repo.create(
            content=content,
        )

    async def get_all(
        self,
        first: int | None = None,
        last: int | None = None,
        after: int | None = None,
        before: int | None = None,
    ) -> PaginatedResult[Todo, int]:
        """Get all todos."""
        return await self._todo_repo.get_all(
            first=first,
            last=last,
            after=after,
            before=before,
        )

    async def delete(self, todo_id: int) -> None:
        """Delete a todo by ID."""
        await self._todo_repo.delete(
            todo_id=todo_id,
        )
