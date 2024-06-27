import pytest
from app.todos.repositories import TodoRepo
from app.todos.services import TodoService


@pytest.fixture
def todo_service(todo_repo: TodoRepo) -> TodoService:
    return TodoService(todo_repo=todo_repo)
