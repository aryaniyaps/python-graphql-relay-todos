import pytest
from app.database.paginator import Paginator
from app.todos.models import Todo
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select


@pytest.fixture
async def todo_paginator(session: AsyncSession) -> Paginator[Todo, int]:
    return Paginator(session, Todo.id)


@pytest.fixture(autouse=True)
async def todos(session: AsyncSession) -> list[Todo]:
    todos = [Todo(content=f"Todo {i}") for i in range(50)]
    session.add_all(todos)
    await session.commit()
    return todos


async def test_paginate_forwards(todo_paginator: Paginator[Todo, int]) -> None:
    # paginate forwards
    result = await todo_paginator.paginate(select(Todo), first=10)

    # check the results
    assert len(result.entities) == 10
    assert result.page_info.has_next_page is True
    assert result.page_info.has_previous_page is False
    assert result.page_info.start_cursor == 1
    assert result.page_info.end_cursor == 10


async def test_paginate_forwards_after(todo_paginator: Paginator[Todo, int]) -> None:
    # paginate forwards
    result = await todo_paginator.paginate(select(Todo), first=10, after=10)

    # check the results
    assert len(result.entities) == 10
    assert result.page_info.has_next_page is True
    assert result.page_info.has_previous_page is True
    assert result.page_info.start_cursor == 11
    assert result.page_info.end_cursor == 20


async def test_paginate_backwards(todo_paginator: Paginator[Todo, int]) -> None:
    # paginate backwards
    result = await todo_paginator.paginate(select(Todo), last=10, after=40)

    # check the results
    assert len(result.entities) == 10
    assert result.page_info.has_next_page is False
    assert result.page_info.has_previous_page is True
    assert result.page_info.start_cursor == 41
    assert result.page_info.end_cursor == 50


async def test_paginate_invalid_arguments(todo_paginator: Paginator[Todo, int]) -> None:
    # test that an error is raised when both `first` and `last` are provided
    with pytest.raises(ValueError):
        await todo_paginator.paginate(select(Todo), first=10, last=10)

    # test that an error is raised when `first` is provided with `before`
    with pytest.raises(ValueError):
        await todo_paginator.paginate(select(Todo), first=10, before=5)

    # test that an error is raised when `last` is provided with `after`
    with pytest.raises(ValueError):
        await todo_paginator.paginate(select(Todo), last=10, after=5)

    # test that an error is raised when `first` exceeds the maximum pagination limit
    with pytest.raises(ValueError):
        await todo_paginator.paginate(select(Todo), first=101)

    # test that an error is raised when `last` exceeds the maximum pagination limit
    with pytest.raises(ValueError):
        await todo_paginator.paginate(select(Todo), last=101)

    # test that an error is raised when neither `first` nor `last` is provided
    with pytest.raises(ValueError):
        await todo_paginator.paginate(select(Todo))


async def test_paginate_empty_results(todo_paginator: Paginator[Todo, int]) -> None:
    # test that an empty result set is returned when there are no matching records
    result = await todo_paginator.paginate(select(Todo).where(Todo.id > 50), first=10)
    assert len(result.entities) == 0
    assert result.page_info.has_next_page is False
    assert result.page_info.has_previous_page is False
    assert result.page_info.start_cursor is None
    assert result.page_info.end_cursor is None


async def test_paginate_single_page(todo_paginator: Paginator[Todo, int]) -> None:
    # test that a single page of results is returned when there are fewer records than the pagination limit
    result = await todo_paginator.paginate(select(Todo), first=75)
    assert len(result.entities) == 50
    assert result.page_info.has_next_page is False
    assert result.page_info.has_previous_page is False
    assert result.page_info.start_cursor == 1
    assert result.page_info.end_cursor == 50


async def test_paginate_last_and_before(todo_paginator: Paginator[Todo, int]) -> None:
    # test that `last` and `before` arguments can be used together
    result = await todo_paginator.paginate(select(Todo), last=10, before=50)
    assert len(result.entities) == 10
    assert result.page_info.has_next_page is False
    assert result.page_info.has_previous_page is True
    assert result.page_info.start_cursor == 41
    assert result.page_info.end_cursor == 50


async def test_paginate_first_and_after(todo_paginator: Paginator[Todo, int]) -> None:
    # test that `first` and `after` arguments can be used together
    result = await todo_paginator.paginate(select(Todo), first=10, after=40)
    assert len(result.entities) == 10
    assert result.page_info.has_next_page is True
    assert result.page_info.has_previous_page is False
    assert result.page_info.start_cursor == 41
    assert result.page_info.end_cursor == 50


async def test_paginate_first_and_before(todo_paginator: Paginator[Todo, int]) -> None:
    # test that an error is raised when `first` and `before` arguments are used together
    with pytest.raises(ValueError):
        await todo_paginator.paginate(select(Todo), first=10, before=50)


async def test_paginate_last_and_after(todo_paginator: Paginator[Todo, int]) -> None:
    # test that an error is raised when `last` and `after` arguments are used together
    with pytest.raises(ValueError):
        await todo_paginator.paginate(select(Todo), last=10, after=50)
