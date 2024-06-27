from typing import Annotated

import strawberry
from aioinject import Inject
from aioinject.ext.strawberry import inject
from strawberry import relay

from app.context import Info

from .services import TodoService
from .types import TodoType


@strawberry.type
class TodoMutation:
    @strawberry.mutation(
        graphql_type=TodoType,
        description="Create a new todo.",
    )
    @inject
    async def create_todo(
        self,
        content: Annotated[
            str,
            strawberry.argument(
                description="The content of the todo.",
            ),
        ],
        todo_service: Annotated[TodoService, Inject],
    ) -> TodoType:
        """Create a new todo."""
        todo = await todo_service.create_todo(
            content=content,
        )
        return TodoType.from_orm(todo)

    @strawberry.mutation(
        graphql_type=None,
        description="Delete a todo by ID.",
    )
    @inject
    async def delete_todo(
        self,
        info: Info,
        todo_id: Annotated[
            relay.GlobalID,
            strawberry.argument(
                description="The ID of the todo to delete.",
            ),
        ],
        todo_service: Annotated[TodoService, Inject],
    ) -> None:
        """Delete a todo by ID."""
        todo = await todo_id.resolve_node(info, ensure_type=TodoType)
        await todo_service.delete(todo_id=int(todo.id))
