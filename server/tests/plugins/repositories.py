import pytest
from app.todos.repositories import TodoRepo
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture
def todo_repo(session: AsyncSession) -> TodoRepo:
    return TodoRepo(
        session=session,
    )
