import pytest
from app.todos.exceptions import TodoNotFoundError
from app.todos.models import Todo
from app.todos.repositories import TodoRepo
from app.todos.services import TodoService
from result import Err, Ok


@pytest.fixture
async def todo(todo_repo: TodoRepo) -> Todo:
    return await todo_repo.create(
        content="test content",
    )


async def test_create_todo(todo_service: TodoService) -> None:
    """Ensure we can create a new todo."""
    result = await todo_service.create(
        content="content",
    )
    assert isinstance(result, Ok)
    assert isinstance(result.ok_value, Todo)
    assert result.ok_value.id is not None
    assert result.ok_value.content == "content"
    assert result.ok_value.created_at is not None
    assert result.ok_value.updated_at is None


async def test_get_all_todos(todo_service: TodoService) -> None:
    """Ensure we can get all todos."""
    pass


async def test_delete_todo(
    todo: Todo,
    todo_service: TodoService,
    todo_repo: TodoRepo,
) -> None:
    """Ensure we can delete a todo by ID."""
    result = await todo_service.delete(todo_id=todo.id)
    assert await todo_repo.get(todo_id=todo.id) is None
    assert isinstance(result, Ok)
    assert result.ok_value == todo


async def test_delete_todo_unknown(todo_service: TodoService) -> None:
    """Ensure we cannot delete an unknown todo by ID."""
    result = await todo_service.delete(todo_id=1432)
    assert isinstance(result, Err)
    assert isinstance(result.err_value, TodoNotFoundError)


async def test_toggle_todo_completed(todo: Todo, todo_service: TodoService) -> None:
    """Ensure we can toggle a todo's completed state by ID."""
    initial_completed_value = todo.completed
    result = await todo_service.toggle_completed(todo_id=todo.id)
    assert isinstance(result, Ok)
    assert result.ok_value.completed == (not initial_completed_value)
    result = await todo_service.toggle_completed(todo_id=todo.id)
    assert isinstance(result, Ok)
    assert result.ok_value.completed == initial_completed_value


async def test_toggle_todo_completed_unknown(todo_service: TodoService) -> None:
    """Ensure we cannot toggle an unknown todo's completed state by ID."""
    result = await todo_service.toggle_completed(todo_id=1432)
    assert isinstance(result, Err)
    assert isinstance(result.err_value, TodoNotFoundError)
