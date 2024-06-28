from typing import Annotated

import strawberry
from aioinject import Inject
from aioinject.ext.strawberry import inject
from result import Err
from strawberry import relay

from .exceptions import TodoNotFoundError
from .services import TodoService
from .types import (
    CreateTodoPayload,
    DeleteTodoPayload,
    TodoNotFoundErrorType,
    TodoType,
    ToggleTodoCompletedPayload,
)


@strawberry.type
class TodoMutation:
    @strawberry.mutation(
        graphql_type=CreateTodoPayload,
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
    ) -> CreateTodoPayload:
        """Create a new todo."""
        todo = await todo_service.create(
            content=content,
        )
        return CreateTodoPayload(
            todo_edge=relay.Edge(
                node=TodoType.from_orm(todo),
                cursor=relay.to_base64(TodoType, todo.id),
            ),
        )

    @strawberry.mutation(
        graphql_type=DeleteTodoPayload,
        description="Delete a todo by ID.",
    )
    @inject
    async def delete_todo(
        self,
        todo_id: Annotated[
            relay.GlobalID,
            strawberry.argument(
                description="The ID of the todo to delete.",
            ),
        ],
        todo_service: Annotated[TodoService, Inject],
    ) -> TodoType | TodoNotFoundErrorType:
        """Delete a todo by ID."""
        result = await todo_service.delete(
            todo_id=int(todo_id.node_id),
        )

        if isinstance(result, Err):
            match result.err_value:
                case TodoNotFoundError():
                    return TodoNotFoundErrorType()

        return TodoType.from_orm(
            todo=result.ok_value,
        )

    @strawberry.mutation(
        graphql_type=ToggleTodoCompletedPayload,
        description="Toggle the completed state of a todo by ID.",
    )
    @inject
    async def toggle_todo_completed(
        self,
        todo_id: Annotated[
            relay.GlobalID,
            strawberry.argument(
                description="The ID of the todo to toggle.",
            ),
        ],
        todo_service: Annotated[TodoService, Inject],
    ) -> TodoType | TodoNotFoundErrorType:
        """Toggle a todo's completed state by ID."""
        result = await todo_service.toggle_completed(
            todo_id=int(todo_id.node_id),
        )

        if isinstance(result, Err):
            match result.err_value:
                case TodoNotFoundError():
                    return TodoNotFoundErrorType()

        return TodoType.from_orm(
            todo=result.ok_value,
        )
