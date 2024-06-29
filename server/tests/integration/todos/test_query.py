import pytest
from app.todos.models import Todo
from app.todos.repositories import TodoRepo
from app.todos.types import TodoType
from sqlalchemy.ext.asyncio import AsyncSession
from strawberry.relay import to_base64

from server.tests.integration.graphql_client import GraphQLClient

pytestmark = pytest.mark.usefixtures("session")


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


GET_TODO_QUERY = """
query GetTodoQuery($todoId: ID!) {
    node(id: $todoId) {
        ...on Todo {
            id
            content
            completed
            createdAt
            updatedAt
        }
    }
}
"""


async def test_get_todo(graphql_client: GraphQLClient, todo: Todo) -> None:
    """Ensure that we can get a todo by ID."""
    response = await graphql_client(
        GET_TODO_QUERY,
        variables={
            "todoId": to_base64(TodoType, todo.id),
        },
    )

    assert response == {
        "data": {
            "node": {
                "id": to_base64(TodoType, todo.id),
                "completed": todo.completed,
                "content": todo.content,
                "createdAt": todo.created_at.isoformat(),
                "updatedAt": todo.updated_at.isoformat() if todo.updated_at else None,
            },
        },
    }


async def test_get_todo_unknown_id(graphql_client: GraphQLClient) -> None:
    """Ensure that we cannot get a todo by unknown ID."""
    response = await graphql_client(
        GET_TODO_QUERY,
        variables={
            "todoId": to_base64(TodoType, 1432),
        },
    )

    assert response == {
        "data": {"node": None},
    }


GET_TODOS_QUERY = """
query GetTodosQuery($first: Int, $last: Int, $after: String, $before: String) {
    todos(first: $first, last: $last, after: $after, before: $before) {
        edges {
            node {
                id
                content
                completed
                createdAt
                updatedAt
            }
            cursor
        }
        pageInfo {
            startCursor
            endCursor
            hasNextPage
            hasPreviousPage
        }
    }
}
"""


@pytest.mark.usefixtures("__seed_todos")
async def test_get_todos(graphql_client: GraphQLClient) -> None:
    """Ensure that we can get all todos."""
    pagination_limit = 10

    # Test fetching the first 10 todos
    response = await graphql_client(
        GET_TODOS_QUERY,
        variables={
            "first": pagination_limit,
        },
    )

    assert len(response["data"]["todos"]["edges"]) == pagination_limit
    assert response["data"]["todos"]["pageInfo"]["hasNextPage"] is True
    assert response["data"]["todos"]["pageInfo"]["hasPreviousPage"] is False
    assert response["data"]["todos"]["pageInfo"]["startCursor"] == to_base64(
        TodoType, 50
    )
    assert response["data"]["todos"]["pageInfo"]["endCursor"] == to_base64(TodoType, 41)

    # Test fetching the next 10 todos
    response = await graphql_client(
        GET_TODOS_QUERY,
        variables={
            "first": pagination_limit,
            "after": to_base64(TodoType, 49),
        },
    )
    assert len(response["data"]["todos"]["edges"]) == pagination_limit
    assert response["data"]["todos"]["pageInfo"]["hasNextPage"] is True
    assert response["data"]["todos"]["pageInfo"]["hasPreviousPage"] is True
    assert response["data"]["todos"]["pageInfo"]["startCursor"] == to_base64(
        TodoType, 48
    )
    assert response["data"]["todos"]["pageInfo"]["endCursor"] == to_base64(TodoType, 39)

    # Test fetching the last 10 todos
    response = await graphql_client(
        GET_TODOS_QUERY,
        variables={"last": pagination_limit},
    )
    assert len(response["data"]["todos"]["edges"]) == pagination_limit
    assert response["data"]["todos"]["pageInfo"]["hasNextPage"] is False
    assert response["data"]["todos"]["pageInfo"]["hasPreviousPage"] is True
    assert response["data"]["todos"]["pageInfo"]["startCursor"] == to_base64(
        TodoType, 10
    )
    assert response["data"]["todos"]["pageInfo"]["endCursor"] == to_base64(TodoType, 1)

    # Test fetching 10 todos before the last one
    response = await graphql_client(
        GET_TODOS_QUERY,
        variables={
            "last": pagination_limit,
            "before": to_base64(TodoType, 1),
        },
    )
    assert len(response["data"]["todos"]["edges"]) == pagination_limit
    assert response["data"]["todos"]["pageInfo"]["hasNextPage"] is True
    assert response["data"]["todos"]["pageInfo"]["hasPreviousPage"] is True
    assert response["data"]["todos"]["pageInfo"]["startCursor"] == to_base64(
        TodoType, 11
    )
    assert response["data"]["todos"]["pageInfo"]["endCursor"] == to_base64(TodoType, 2)

    # Test fetching all todos with a limit higher than the total count
    pagination_limit = 75

    response = await graphql_client(
        GET_TODOS_QUERY,
        variables={
            "first": pagination_limit,
        },
    )
    assert len(response["data"]["todos"]["edges"]) < pagination_limit
    assert response["data"]["todos"]["pageInfo"]["hasNextPage"] is False
    assert response["data"]["todos"]["pageInfo"]["hasPreviousPage"] is False
    assert response["data"]["todos"]["pageInfo"]["startCursor"] == to_base64(
        TodoType, 50
    )
    assert response["data"]["todos"]["pageInfo"]["endCursor"] == to_base64(TodoType, 1)
