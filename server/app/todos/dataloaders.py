from sqlalchemy import select

from app.database.session import async_session_factory

from .models import Todo


async def load_todo_by_id(
    todo_ids: list[str],
) -> list[Todo | None]:
    stmt = select(Todo).where(Todo.id.in_(todo_ids))

    async with async_session_factory() as session:
        todo_by_id = {str(todo.id): todo for todo in await session.scalars(stmt)}

    return [todo_by_id.get(str(todo_id)) for todo_id in todo_ids]
