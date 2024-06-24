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

    async def get_all(self) -> list[Todo]:
        """Get all todos."""
        return await self._todo_repo.get_all()

    async def delete(self, todo_id: str) -> None:
        """Delete a todo by ID."""
        await self._todo_repo.delete(
            todo_id=todo_id,
        )
