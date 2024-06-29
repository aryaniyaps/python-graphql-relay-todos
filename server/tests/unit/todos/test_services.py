import pytest
from app.todos.exceptions import TodoNotFoundError
from app.todos.models import Todo
from app.todos.repositories import TodoRepo
from app.todos.services import TodoService
from result import Err, Ok
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture
async def todo(todo_repo: TodoRepo) -> Todo:
    return await todo_repo.create(
        content="test content",
    )


@pytest.fixture
async def __seed_todos(session: AsyncSession) -> None:
    todos = [
        Todo(
            content=f"Todo {i}",
            id=i + 1,
        )
        for i in range(50)
    ]
    session.add_all(todos)
    await session.commit()


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


@pytest.mark.usefixtures("__seed_todos")
async def test_get_all_todos(todo_service: TodoService) -> None:
    """Ensure we can get all todos."""
    pagination_limit = 10

    # Test fetching the first 10 todos
    paginated_result = await todo_service.get_all(first=pagination_limit)
    assert len(paginated_result.entities) == pagination_limit
    assert paginated_result.page_info.has_next_page is True
    assert paginated_result.page_info.has_previous_page is False
    assert paginated_result.page_info.start_cursor == 50
    assert paginated_result.page_info.end_cursor == 41

    # Test fetching the next 10 todos
    paginated_result = await todo_service.get_all(first=pagination_limit, after=49)
    assert len(paginated_result.entities) == pagination_limit
    assert paginated_result.page_info.has_next_page is True
    assert paginated_result.page_info.has_previous_page is True
    assert paginated_result.page_info.start_cursor == 48
    assert paginated_result.page_info.end_cursor == 39

    # Test fetching the last 10 todos
    paginated_result = await todo_service.get_all(last=pagination_limit)
    assert len(paginated_result.entities) == pagination_limit
    assert paginated_result.page_info.has_next_page is False
    assert paginated_result.page_info.has_previous_page is True
    assert paginated_result.page_info.start_cursor == 10
    assert paginated_result.page_info.end_cursor == 1

    # Test fetching 10 todos before the last one
    paginated_result = await todo_service.get_all(last=pagination_limit, before=1)
    assert len(paginated_result.entities) == pagination_limit
    assert paginated_result.page_info.has_next_page is True
    assert paginated_result.page_info.has_previous_page is True
    assert paginated_result.page_info.start_cursor == 11
    assert paginated_result.page_info.end_cursor == 2

    # Test fetching all todos with a limit higher than the total count
    pagination_limit = 75

    paginated_result = await todo_service.get_all(first=pagination_limit)
    assert len(paginated_result.entities) < pagination_limit
    assert paginated_result.page_info.has_next_page is False
    assert paginated_result.page_info.has_previous_page is False
    assert paginated_result.page_info.start_cursor == 50
    assert paginated_result.page_info.end_cursor == 1


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
