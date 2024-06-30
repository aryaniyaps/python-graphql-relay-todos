from result import Err, Ok, Result

from .exceptions import TodoNotFoundError
from .models import Todo
from .repositories import TodoRepo


class TodoService:
    def __init__(self, todo_repo: TodoRepo) -> None:
        self._todo_repo = todo_repo

    async def create(self, content: str) -> Result[Todo, None]:
        """Create a new todo."""
        return Ok(
            await self._todo_repo.create(
                content=content,
            )
        )

    async def delete(self, todo_id: int) -> Result[Todo, TodoNotFoundError]:
        """Delete a todo by ID."""
        existing_todo = await self._todo_repo.get(todo_id=todo_id)
        if existing_todo is None:
            return Err(TodoNotFoundError())
        await self._todo_repo.delete(
            todo=existing_todo,
        )
        return Ok(existing_todo)

    async def toggle_completed(self, todo_id: int) -> Result[Todo, TodoNotFoundError]:
        """Toggle a todo's completed state by ID."""
        existing_todo = await self._todo_repo.get(todo_id=todo_id)
        if existing_todo is None:
            return Err(TodoNotFoundError())
        return Ok(
            await self._todo_repo.update(
                todo=existing_todo,
                completed=(not existing_todo.completed),
            )
        )
