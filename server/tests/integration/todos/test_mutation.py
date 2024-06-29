import pytest
from app.todos.models import Todo
from app.todos.types import TodoType
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from strawberry import relay

from tests.integration.client import GraphQLClient

pytestmark = pytest.mark.usefixtures("session")

CREATE_TODO_MUTATION = """
mutation CreateTodo($content: String!) {
    createTodo(content: $content) {
        todoEdge {
            node {
                id
                content
                completed
                createdAt
                updatedAt
            }
            cursor
        }
    }
}
"""


async def test_create_todo(
    graphql_client: GraphQLClient,
    session: AsyncSession,
) -> None:
    """Ensure that we can create a todo."""
    content = "test content"
    response = await graphql_client(
        CREATE_TODO_MUTATION,
        variables={
            "content": content,
        },
    )

    todo = (await session.scalars(select(Todo))).one()

    assert response == {
        "data": {
            "createTodo": {
                "todoEdge": {
                    "node": {
                        "id": relay.to_base64(TodoType, todo.id),
                        "completed": todo.completed,
                        "content": content,
                        "createdAt": todo.created_at.isoformat(),
                        "updatedAt": todo.updated_at.isoformat()
                        if todo.updated_at
                        else None,
                    },
                    "cursor": relay.to_base64(TodoType, todo.id),
                },
            },
        },
    }


DELETE_TODO_MUTATION = """
mutation DeleteTodo($todoId: ID!) {
    deleteTodo(todoId: $todoId) {
        __typename
        ... on Todo {
            id
            content
            completed
            createdAt
            updatedAt
        }
        ... on TodoNotFoundError {
            message
        }
    }
}
"""


async def test_delete_todo(
    graphql_client: GraphQLClient,
    todo: Todo,
    session: AsyncSession,
) -> None:
    """Ensure that we can delete a todo."""
    response = await graphql_client(
        DELETE_TODO_MUTATION,
        variables={
            "todoId": relay.to_base64(TodoType, todo.id),
        },
    )

    result = await session.scalar(
        select(Todo).where(Todo.id == todo.id),
    )

    assert result is None

    assert response == {
        "data": {
            "deleteTodo": {
                "__typename": "Todo",
                "id": relay.to_base64(TodoType, todo.id),
                "completed": todo.completed,
                "content": todo.content,
                "createdAt": todo.created_at.isoformat(),
                "updatedAt": todo.updated_at.isoformat() if todo.updated_at else None,
            },
        },
    }


async def test_delete_todo_unknown_id(graphql_client: GraphQLClient) -> None:
    """Ensure that we cannot delete a todo with an unknown ID."""
    response = await graphql_client(
        DELETE_TODO_MUTATION,
        variables={
            "todoId": relay.to_base64(TodoType, 1432),
        },
    )

    assert response == {
        "data": {
            "deleteTodo": {
                "__typename": "TodoNotFoundError",
                "message": "Todo does not exist",
            },
        },
    }


TOGGLE_TODO_COMPLETED_MUTATION = """
mutation ToggleTodoCompleted($todoId: ID!) {
    toggleTodoCompleted(todoId: $todoId) {
        __typename
        ... on Todo {
            id
            content
            completed
            createdAt
            updatedAt
        }
        ... on TodoNotFoundError {
            message
        }
    }
}
"""


async def test_toggle_todo_completed(
    graphql_client: GraphQLClient,
    todo: Todo,
    session: AsyncSession,
) -> None:
    """Ensure that we can toggle a todo's completed state."""
    initial_completed_value = todo.completed
    response = await graphql_client(
        TOGGLE_TODO_COMPLETED_MUTATION,
        variables={
            "todoId": relay.to_base64(TodoType, todo.id),
        },
    )

    await session.refresh(todo)
    assert todo.completed == (not initial_completed_value)

    assert response == {
        "data": {
            "toggleTodoCompleted": {
                "__typename": "Todo",
                "id": relay.to_base64(TodoType, todo.id),
                "completed": (not initial_completed_value),
                "content": todo.content,
                "createdAt": todo.created_at.isoformat(),
                "updatedAt": todo.updated_at.isoformat() if todo.updated_at else None,
            },
        },
    }


async def test_toggle_todo_completed_unknown_id(graphql_client: GraphQLClient) -> None:
    """Ensure that we cannot toggle a todo's completed state with an unknown ID."""
    response = await graphql_client(
        TOGGLE_TODO_COMPLETED_MUTATION,
        variables={
            "todoId": relay.to_base64(TodoType, 1432),
        },
    )

    assert response == {
        "data": {
            "toggleTodoCompleted": {
                "__typename": "TodoNotFoundError",
                "message": "Todo does not exist",
            },
        },
    }
