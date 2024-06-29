import pytest
from app.todos.models import Todo
from app.todos.types import TodoType
from strawberry import relay

from tests.integration.client import GraphQLClient

pytestmark = pytest.mark.usefixtures("session")

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
            "todoId": relay.to_base64(TodoType, todo.id),
        },
    )

    assert response == {
        "data": {
            "node": {
                "id": relay.to_base64(TodoType, todo.id),
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
            "todoId": relay.to_base64(TodoType, 1432),
        },
    )

    assert response == {
        "data": {"node": None},
    }


GET_TODOS_QUERY = """
query GetTodosQuery($first: Int, $last: Int, after: String, before: String) {
    todos(first: $first, last: $last, after: $after, before: $before) {
        nodes {
            edge {
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
