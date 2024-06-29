import pytest
from app.database.paginator import Paginator
from app.lib.constants import MAX_PAGINATION_LIMIT
from app.todos.models import Todo
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select


@pytest.fixture
async def todo_paginator(session: AsyncSession) -> Paginator[Todo, int]:
    return Paginator(
        session=session,
        paginate_by=Todo.id,
    )


@pytest.fixture
async def reverse_todo_paginator(session: AsyncSession) -> Paginator[Todo, int]:
    return Paginator(
        session=session,
        paginate_by=Todo.id,
        reverse=True,
    )


@pytest.fixture(autouse=True)
async def _seed_todos(session: AsyncSession) -> None:
    todos = [
        Todo(
            content=f"Todo {i}",
            id=i + 1,
            # 50% todos are completed
            completed=i % 2 == 0,
        )
        for i in range(50)
    ]
    session.add_all(todos)
    await session.commit()


async def test_paginate_first(todo_paginator: Paginator[Todo, int]) -> None:
    """Ensure that we can paginate correctly with the `first` argument."""
    pagination_limit = 10
    expected_start_cursor, expected_end_cursor = 1, 10
    result = await todo_paginator.paginate(
        statement=select(Todo), first=pagination_limit
    )

    # check the results
    assert len(result.entities) == pagination_limit
    assert result.page_info.has_next_page is True
    assert result.page_info.has_previous_page is False
    assert result.page_info.start_cursor == expected_start_cursor
    assert result.page_info.end_cursor == expected_end_cursor


async def test_paginate_first_and_after(todo_paginator: Paginator[Todo, int]) -> None:
    """Ensure that we can paginate correctly with the `first` and `after` arguments."""
    pagination_limit = 10
    expected_start_cursor, expected_end_cursor = 11, 20
    result = await todo_paginator.paginate(
        statement=select(Todo), first=pagination_limit, after=10
    )

    # check the results
    assert len(result.entities) == pagination_limit
    assert result.page_info.has_next_page is True
    assert result.page_info.has_previous_page is True
    assert result.page_info.start_cursor == expected_start_cursor
    assert result.page_info.end_cursor == expected_end_cursor


async def test_paginate_last(todo_paginator: Paginator[Todo, int]) -> None:
    """Ensure that we can paginate correctly with the `last` argument."""
    pagination_limit = 10
    expected_start_cursor, expected_end_cursor = 41, 50
    result = await todo_paginator.paginate(
        statement=select(Todo), last=pagination_limit
    )

    # check the results
    assert len(result.entities) == pagination_limit
    assert result.page_info.has_next_page is False
    assert result.page_info.has_previous_page is True
    assert result.page_info.start_cursor == expected_start_cursor
    assert result.page_info.end_cursor == expected_end_cursor


async def test_paginate_last_and_before(todo_paginator: Paginator[Todo, int]) -> None:
    """Ensure that we can paginate correctly with the `last` and `before` arguments."""
    pagination_limit = 10
    expected_start_cursor, expected_end_cursor = 40, 49
    result = await todo_paginator.paginate(
        statement=select(Todo), last=pagination_limit, before=50
    )

    # check the results
    assert len(result.entities) == pagination_limit
    assert result.page_info.has_next_page is True
    assert result.page_info.has_previous_page is True
    assert result.page_info.start_cursor == expected_start_cursor
    assert result.page_info.end_cursor == expected_end_cursor


async def test_paginate_empty_results(todo_paginator: Paginator[Todo, int]) -> None:
    """Test pagination when no records are returned from the database."""
    last_todo_id = 50
    result = await todo_paginator.paginate(
        statement=select(Todo).where(Todo.id > last_todo_id), first=10
    )

    # check the results
    assert len(result.entities) == 0
    assert result.page_info.has_next_page is False
    assert result.page_info.has_previous_page is False
    assert result.page_info.start_cursor is None
    assert result.page_info.end_cursor is None


async def test_paginate_end_page_forwards(todo_paginator: Paginator[Todo, int]) -> None:
    """Test pagination when we've reached the end page forwards."""
    pagination_limit = 75
    expected_start_cursor, expected_end_cursor = 1, 50
    result = await todo_paginator.paginate(
        statement=select(Todo), first=pagination_limit
    )

    # check the results
    assert len(result.entities) < pagination_limit
    assert result.page_info.has_next_page is False
    assert result.page_info.has_previous_page is False
    assert result.page_info.start_cursor == expected_start_cursor
    assert result.page_info.end_cursor == expected_end_cursor


async def test_paginate_end_page_backwards(
    todo_paginator: Paginator[Todo, int],
) -> None:
    """Test pagination when we've reached the end page backwards."""
    pagination_limit = 75
    expected_start_cursor, expected_end_cursor = 1, 50
    result = await todo_paginator.paginate(
        statement=select(Todo), last=pagination_limit
    )

    # check the results
    assert len(result.entities) < pagination_limit
    assert result.page_info.has_next_page is False
    assert result.page_info.has_previous_page is False
    assert result.page_info.start_cursor == expected_start_cursor
    assert result.page_info.end_cursor == expected_end_cursor


async def test_paginate_filter_condition(
    session: AsyncSession, todo_paginator: Paginator[Todo, int]
) -> None:
    """Ensure that filter conditions are preserved while paginating."""
    pagination_limit = 10
    completed_todos = await session.scalars(select(Todo).filter(Todo.completed == True))
    completed_todo_count = len(completed_todos.all())
    result = await todo_paginator.paginate(
        statement=select(Todo).filter(Todo.completed == True),
        first=pagination_limit,
    )

    # check the results
    assert len(result.entities) == min(pagination_limit, completed_todo_count)


# reverse pagination tests


async def test_paginate_reverse_first(
    reverse_todo_paginator: Paginator[Todo, int],
) -> None:
    """Ensure that we can paginate correctly with the `first` argument."""
    pagination_limit = 10
    expected_start_cursor, expected_end_cursor = 50, 41
    result = await reverse_todo_paginator.paginate(
        statement=select(Todo), first=pagination_limit
    )

    # check the results
    assert len(result.entities) == pagination_limit
    assert result.page_info.has_next_page is True
    assert result.page_info.has_previous_page is False
    assert result.page_info.start_cursor == expected_start_cursor
    assert result.page_info.end_cursor == expected_end_cursor


async def test_paginate_reverse_first_and_after(
    reverse_todo_paginator: Paginator[Todo, int],
) -> None:
    """Ensure that we can paginate correctly with the `first` and `after` arguments."""
    pagination_limit = 10
    expected_start_cursor, expected_end_cursor = 40, 31
    result = await reverse_todo_paginator.paginate(
        statement=select(Todo), first=pagination_limit, after=41
    )

    # check the results
    assert len(result.entities) == pagination_limit
    assert result.page_info.has_next_page is True
    assert result.page_info.has_previous_page is True
    assert result.page_info.start_cursor == expected_start_cursor
    assert result.page_info.end_cursor == expected_end_cursor


async def test_paginate_reverse_last(
    reverse_todo_paginator: Paginator[Todo, int],
) -> None:
    """Ensure that we can paginate correctly with the `last` argument."""
    pagination_limit = 10
    expected_start_cursor, expected_end_cursor = 10, 1
    result = await reverse_todo_paginator.paginate(
        statement=select(Todo), last=pagination_limit
    )

    # check the results
    assert len(result.entities) == pagination_limit
    assert result.page_info.has_next_page is False
    assert result.page_info.has_previous_page is True
    assert result.page_info.start_cursor == expected_start_cursor
    assert result.page_info.end_cursor == expected_end_cursor


async def test_paginate_reverse_last_and_before(
    reverse_todo_paginator: Paginator[Todo, int],
) -> None:
    """Ensure that we can paginate correctly with the `last` and `before` arguments."""
    pagination_limit = 10
    expected_start_cursor, expected_end_cursor = 11, 2
    result = await reverse_todo_paginator.paginate(
        statement=select(Todo), last=pagination_limit, before=1
    )

    # check the results
    assert len(result.entities) == pagination_limit
    assert result.page_info.has_next_page is True
    assert result.page_info.has_previous_page is True
    assert result.page_info.start_cursor == expected_start_cursor
    assert result.page_info.end_cursor == expected_end_cursor


async def test_paginate_reverse_empty_results(
    reverse_todo_paginator: Paginator[Todo, int],
) -> None:
    """Test pagination when no records are returned from the database."""
    last_todo_id = 50
    result = await reverse_todo_paginator.paginate(
        statement=select(Todo).where(Todo.id > last_todo_id), first=10
    )

    # check the results
    assert len(result.entities) == 0
    assert result.page_info.has_next_page is False
    assert result.page_info.has_previous_page is False
    assert result.page_info.start_cursor is None
    assert result.page_info.end_cursor is None


async def test_paginate_reverse_end_page_forwards(
    reverse_todo_paginator: Paginator[Todo, int],
) -> None:
    """Test pagination when we've reached the end page forwards."""
    pagination_limit = 75
    expected_start_cursor, expected_end_cursor = 50, 1
    result = await reverse_todo_paginator.paginate(
        statement=select(Todo), first=pagination_limit
    )

    # check the results
    assert len(result.entities) < pagination_limit
    assert result.page_info.has_next_page is False
    assert result.page_info.has_previous_page is False
    assert result.page_info.start_cursor == expected_start_cursor
    assert result.page_info.end_cursor == expected_end_cursor


async def test_paginate_reverse_end_page_backwards(
    reverse_todo_paginator: Paginator[Todo, int],
) -> None:
    """Test pagination when we've reached the end page backwards."""
    pagination_limit = 75
    expected_start_cursor, expected_end_cursor = 50, 1
    result = await reverse_todo_paginator.paginate(
        statement=select(Todo), last=pagination_limit
    )

    # check the results
    assert len(result.entities) < pagination_limit
    assert result.page_info.has_next_page is False
    assert result.page_info.has_previous_page is False
    assert result.page_info.start_cursor == expected_start_cursor
    assert result.page_info.end_cursor == expected_end_cursor


async def test_paginate_reverse_filter_condition(
    session: AsyncSession, reverse_todo_paginator: Paginator[Todo, int]
) -> None:
    """Ensure that filter conditions are preserved while paginating."""
    pagination_limit = 10
    completed_todos = await session.scalars(select(Todo).filter(Todo.completed == True))
    completed_todo_count = len(completed_todos.all())
    result = await reverse_todo_paginator.paginate(
        statement=select(Todo).filter(Todo.completed == True),
        first=pagination_limit,
    )

    # check the results
    assert len(result.entities) == min(pagination_limit, completed_todo_count)


async def test_paginate_invalid_arguments(todo_paginator: Paginator[Todo, int]) -> None:
    """Ensure that we cannot paginate with invalid pagination arguments."""
    # test that an error is raised when both `first` and `last` are provided
    with pytest.raises(ValueError, match="Cannot provide both `first` and `last`"):
        await todo_paginator.paginate(statement=select(Todo), first=10, last=10)

    # test that an error is raised when both `after` and `before` are provided
    with pytest.raises(ValueError, match="Cannot provide both `after` and `before`"):
        await todo_paginator.paginate(
            statement=select(Todo), after=10, before=50, first=10
        )

    # test that an error is raised when `first` is provided with `before`
    with pytest.raises(ValueError, match="`first` cannot be provided with `before`"):
        await todo_paginator.paginate(statement=select(Todo), first=10, before=5)

    # test that an error is raised when `last` is provided with `after`
    with pytest.raises(ValueError, match="`last` cannot be provided with `after`"):
        await todo_paginator.paginate(statement=select(Todo), last=10, after=5)

    # test that an error is raised when `first` exceeds the maximum pagination limit
    with pytest.raises(
        ValueError,
        match=f"`first` exceeds pagination limit of {MAX_PAGINATION_LIMIT} records",
    ):
        await todo_paginator.paginate(
            statement=select(Todo),
            first=MAX_PAGINATION_LIMIT + 1,
        )

    # test that an error is raised when `last` exceeds the maximum pagination limit
    with pytest.raises(
        ValueError,
        match=f"`last` exceeds pagination limit of {MAX_PAGINATION_LIMIT} records",
    ):
        await todo_paginator.paginate(
            statement=select(Todo),
            last=MAX_PAGINATION_LIMIT + 1,
        )

    # test that an error is raised when neither `first` nor `last` is provided
    with pytest.raises(
        ValueError, match="You must provide either `first` or `last` to paginate"
    ):
        await todo_paginator.paginate(statement=select(Todo), first=None, last=None)

    # test that an error is raised when `first` is negative.
    with pytest.raises(ValueError, match="`first` must be a positive integer"):
        await todo_paginator.paginate(statement=select(Todo), first=-10)

    # test that an error is raised when `last` is negative.
    with pytest.raises(ValueError, match="`last` must be a positive integer"):
        await todo_paginator.paginate(statement=select(Todo), last=-10)
