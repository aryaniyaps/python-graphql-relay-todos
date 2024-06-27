import pytest
from app.todos.models import Todo
from app.todos.repositories import TodoRepo
from app.todos.services import TodoService


@pytest.fixture
async def todo(todo_repo: TodoRepo) -> Todo:
    return await todo_repo.create(
        content="test content",
    )


async def test_create_todo(todo_service: TodoService) -> None:
    """Ensure we can create a new todo."""
    todo = await todo_service.create(
        content="content",
    )
    assert isinstance(todo, Todo)
    assert todo.id is not None
    assert todo.content == "content"
    assert todo.created_at is not None
    assert todo.updated_at is None


async def test_get_all_todos(todo_service: TodoService) -> None:
    """Ensure we can get all todos."""
    pass


async def test_delete_todo(
    todo: Todo,
    todo_service: TodoService,
    todo_repo: TodoRepo,
) -> None:
    """Ensure we can delete a todo by ID."""
    await todo_service.delete(todo_id=todo.id)
    assert await todo_repo.get(todo_id=todo.id) is None
