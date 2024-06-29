from app.todos.models import Todo
from app.todos.types import TodoType
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from strawberry import relay

from tests.integration.client import GraphQLClient

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
                        "updatedAt": None,
                    },
                    "cursor": relay.to_base64(TodoType, todo.id),
                },
            },
        },
    }
