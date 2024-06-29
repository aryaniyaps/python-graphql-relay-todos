import pytest
from app.todos.models import Todo
from app.todos.repositories import TodoRepo
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture
async def todo(todo_repo: TodoRepo) -> Todo:
    return await todo_repo.create(
        content="test content",
    )


@pytest.fixture
async def multiple_todos(todo_repo: TodoRepo) -> list[Todo]:
    todo_1 = await todo_repo.create(content="test content 1")
    todo_2 = await todo_repo.create(content="test content 2")
    todo_3 = await todo_repo.create(content="test content 3")
    todo_4 = await todo_repo.create(content="test content 4")
    return [todo_1, todo_2, todo_3, todo_4]


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


async def test_get_multiple_todos_by_ids(
    multiple_todos: list[Todo], todo_repo: TodoRepo
) -> None:
    """Ensure we can get multiple todos by IDs."""
    todo_ids = [todo.id for todo in multiple_todos]
    todos = await todo_repo.get_many_by_ids(todo_ids=todo_ids)
    assert len(todos) == len(todo_ids)
    for original, retrieved in zip(multiple_todos, todos, strict=True):
        assert retrieved == original


async def test_get_all_todos(todo_repo: TodoRepo, session: AsyncSession) -> None:
    """Ensure we can get all todos."""
    # Create multiple todos for testing
    todos = [
        Todo(
            content=f"Todo {i}",
            id=i + 1,
        )
        for i in range(50)
    ]
    session.add_all(todos)
    await session.commit()

    pagination_limit = 10

    # Test fetching the first 10 todos
    paginated_result = await todo_repo.get_all(first=pagination_limit)
    assert len(paginated_result.entities) == pagination_limit
    assert paginated_result.page_info.has_next_page is True
    assert paginated_result.page_info.has_previous_page is False
    assert paginated_result.page_info.start_cursor == 50
    assert paginated_result.page_info.end_cursor == 41

    # Test fetching the next 10 todos
    paginated_result = await todo_repo.get_all(first=pagination_limit, after=49)
    assert len(paginated_result.entities) == pagination_limit
    assert paginated_result.page_info.has_next_page is True
    assert paginated_result.page_info.has_previous_page is True
    assert paginated_result.page_info.start_cursor == 48
    assert paginated_result.page_info.end_cursor == 39

    # Test fetching the last 10 todos
    paginated_result = await todo_repo.get_all(last=pagination_limit)
    assert len(paginated_result.entities) == pagination_limit
    assert paginated_result.page_info.has_next_page is False
    assert paginated_result.page_info.has_previous_page is True
    assert paginated_result.page_info.start_cursor == 10
    assert paginated_result.page_info.end_cursor == 1

    # Test fetching 10 todos before the last one
    paginated_result = await todo_repo.get_all(last=pagination_limit, before=1)
    assert len(paginated_result.entities) == pagination_limit
    assert paginated_result.page_info.has_next_page is True
    assert paginated_result.page_info.has_previous_page is True
    assert paginated_result.page_info.start_cursor == 11
    assert paginated_result.page_info.end_cursor == 2

    # Test fetching all todos with a limit higher than the total count
    pagination_limit = 75

    paginated_result = await todo_repo.get_all(first=pagination_limit)
    assert len(paginated_result.entities) < pagination_limit
    assert paginated_result.page_info.has_next_page is False
    assert paginated_result.page_info.has_previous_page is False
    assert paginated_result.page_info.start_cursor == 50
    assert paginated_result.page_info.end_cursor == 1


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
