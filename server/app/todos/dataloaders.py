from typing import Annotated

from aioinject import Inject
from aioinject.ext.strawberry import inject

from app.todos.repositories import TodoRepo

from .models import Todo


@inject
async def load_todo_by_id(
    todo_ids: list[str],
    todo_repo: Annotated[
        TodoRepo,
        Inject,
    ],
) -> list[Todo | None]:
    """Load multiple todos by their IDs."""
    return await todo_repo.get_by_ids(
        todo_ids=list(map(int, todo_ids)),
    )
