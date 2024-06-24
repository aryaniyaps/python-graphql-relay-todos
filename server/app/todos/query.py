from typing import Annotated

import strawberry
from aioinject import Inject
from aioinject.ext.strawberry import inject
from strawberry import relay

from .services import TodoService
from .types import TodoType


# TODO: add viewer type which returns todos maybe, so that we can use fragments easily in the client
@strawberry.type
class TodoQuery:
    @relay.connection(
        graphql_type=relay.ListConnection[TodoType],
    )
    @inject
    async def todos(
        self,
        todo_service: Annotated[TodoService, Inject],
    ) -> list[TodoType]:
        todos = await todo_service.get_all()

        return [
            TodoType(
                id=str(todo.id),
                created_at=todo.created_at,
                content=todo.content,
                updated_at=todo.updated_at,
            )
            for todo in todos
        ]
