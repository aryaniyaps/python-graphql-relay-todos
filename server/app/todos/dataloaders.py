from aioinject import inject
from sqlalchemy import select

from app.database.session import async_session_factory

from .models import Todo


# @inject
async def load_todo_by_id(
    todo_ids: list[str],
) -> list[Todo | None]:
    int_todo_ids = list(map(int, todo_ids))
    stmt = select(Todo).where(Todo.id.in_(int_todo_ids))

    async with async_session_factory() as session:
        todo_by_id = {todo.id: todo for todo in await session.scalars(stmt)}

    return [todo_by_id.get(todo_id) for todo_id in int_todo_ids]
