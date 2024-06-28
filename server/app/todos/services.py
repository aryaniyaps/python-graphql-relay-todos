from app.database.paginator import PaginatedResult

from .models import Todo
from .repositories import TodoRepo


class TodoService:
    def __init__(self, todo_repo: TodoRepo) -> None:
        self._todo_repo = todo_repo

    async def create(self, content: str) -> Todo:
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
        existing_todo = await self._todo_repo.get(todo_id=todo_id)
        if existing_todo is None:
            raise ValueError("Todo doesn't exist.")
        await self._todo_repo.delete(
            todo=existing_todo,
        )

    async def toggle_completed(self, todo_id: int) -> Todo:
        """Toggle a todo's completed state by ID."""
        existing_todo = await self._todo_repo.get(todo_id=todo_id)
        if existing_todo is None:
            raise ValueError("Todo doesn't exist.")
        return await self._todo_repo.update(
            todo=existing_todo,
            completed=(not existing_todo.completed),
        )
