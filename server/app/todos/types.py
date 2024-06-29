from collections.abc import Iterable
from datetime import datetime
from typing import Annotated, Self

import strawberry
from strawberry import relay

from app.base.types import BaseErrorType, BaseNodeType
from app.context import Info
from app.database.paginator import PaginatedResult
from app.todos.models import Todo


@strawberry.type(name="Todo")
class TodoType(BaseNodeType[Todo]):
    content: str
    completed: bool
    created_at: datetime
    updated_at: datetime | None

    @classmethod
    def from_orm(cls, todo: Todo) -> Self:
        """Construct a node from an ORM instance."""
        return cls(
            id=todo.id,
            content=todo.content,
            completed=todo.completed,
            created_at=todo.created_at,
            updated_at=todo.updated_at,
        )

    @classmethod
    async def resolve_nodes(  # type: ignore[no-untyped-def] # noqa: ANN206
        cls,
        *,
        info: Info,
        node_ids: Iterable[str],
        required: bool = False,  # noqa: ARG003
    ):
        todos = await info.context.loaders.todo_by_id.load_many(node_ids)
        return [cls.from_orm(todo) if todo is not None else todo for todo in todos]


@strawberry.type(name="TodoNotFoundError")
class TodoNotFoundErrorType(BaseErrorType):
    message: str = "Todo does not exist"


@strawberry.type
class CreateTodoPayload:
    todo_edge: relay.Edge[TodoType]


ToggleTodoCompletedPayload = Annotated[
    TodoType | TodoNotFoundErrorType,
    strawberry.union(name="ToggleTodoCompletedPayload"),
]

DeleteTodoPayload = Annotated[
    TodoType | TodoNotFoundErrorType,
    strawberry.union(name="DeleteTodoPayload"),
]


@strawberry.type(name="TodoConnection")
class TodoConnectionType(relay.Connection[TodoType]):
    @classmethod
    def from_paginated_result(
        cls, paginated_result: PaginatedResult[Todo, int]
    ) -> Self:
        return cls(
            page_info=relay.PageInfo(
                has_next_page=paginated_result.page_info.has_next_page,
                start_cursor=relay.to_base64(
                    TodoType,
                    paginated_result.page_info.start_cursor,
                ),
                has_previous_page=paginated_result.page_info.has_previous_page,
                end_cursor=relay.to_base64(
                    TodoType,
                    paginated_result.page_info.end_cursor,
                ),
            ),
            edges=[
                relay.Edge(
                    node=TodoType.from_orm(todo),
                    cursor=relay.to_base64(TodoType, todo.id),
                )
                for todo in paginated_result.entities
            ],
        )
