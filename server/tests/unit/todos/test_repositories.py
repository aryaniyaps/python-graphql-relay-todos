import pytest
from app.todos.models import Todo
from app.todos.repositories import TodoRepo


@pytest.fixture
async def todo(todo_repo: TodoRepo) -> Todo:
    return await todo_repo.create(
        content="test content",
    )


async def test_create_todo(todo_repo: TodoRepo) -> None:
    """Ensure we can create a new todo."""
    todo = await todo_repo.create(
        content="content",
    )
    assert isinstance(todo, Todo)
    assert todo.id is not None
    assert todo.content == "content"
    assert not todo.completed
    assert todo.created_at is not None
    assert todo.updated_at is None


async def test_get_todo_by_id(todo: Todo, todo_repo: TodoRepo) -> None:
    """Ensure we can get a todo by ID."""
    retrieved_todo = await todo_repo.get(todo_id=todo.id)
    assert retrieved_todo is not None
    assert retrieved_todo == todo


async def test_get_todo_by_unknown_id(todo_repo: TodoRepo) -> None:
    """Ensure we cannot get a todo by unknown ID."""
    retrieved_todo = await todo_repo.get(todo_id=1432)
    assert retrieved_todo is None


async def test_get_multiple_todos_by_ids(todo: Todo, todo_repo: TodoRepo) -> None:
    """Ensure we can get multiple todos by IDs."""
    pass


async def test_get_all_todos(todo_repo: TodoRepo) -> None:
    """Ensure we can get all todos."""
    pass


async def test_delete_todo(todo: Todo, todo_repo: TodoRepo) -> None:
    """Ensure we can delete a todo."""
    await todo_repo.delete(todo=todo)
    assert await todo_repo.get(todo_id=todo.id) is None


async def test_update_todo(todo: Todo, todo_repo: TodoRepo) -> None:
    """Ensure we can update a todo."""
    initial_completed_value = todo.completed
    # mark todo as complete
    await todo_repo.update(todo=todo, completed=True)
    assert todo.completed == (not initial_completed_value)
    assert todo.updated_at is not None

    # mark todo as incomplete
    await todo_repo.update(todo=todo, completed=False)
    assert todo.completed == initial_completed_value
    assert todo.updated_at is not None
