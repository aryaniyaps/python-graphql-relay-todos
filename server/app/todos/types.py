from collections.abc import Iterable
from datetime import datetime
from typing import Self

import strawberry
from strawberry import relay
from strawberry.relay.types import NodeIterableType

from app.context import Info
from app.database.paginator import PaginatedResult


@strawberry.type(name="Todo")
class TodoType(relay.Node):
    id: relay.NodeID[str]
    content: str
    created_at: datetime
    updated_at: datetime | None

    @classmethod
    async def resolve_nodes(
        cls,
        *,
        info: Info,
        node_ids: Iterable[str],
        required: bool = False,
    ) -> NodeIterableType[Self | None]:
        return await info.context.loaders.todo_by_id.load_many(node_ids)


@strawberry.type(name="TodoConnection")
class TodoConnectionType(relay.Connection[TodoType]):
    @classmethod
    def from_paginated_result(cls, paginated_result: PaginatedResult) -> Self:
        return cls(
            page_info=relay.PageInfo(
                has_next_page=paginated_result.page_info.has_next_page,
                start_cursor=relay.to_base64(
                    TodoType,
                    paginated_result.page_info.start_cursor,
                ),
                has_previous_page=False,
                end_cursor=None,
            ),
            edges=[
                relay.Edge(
                    node=TodoType(
                        id=todo.id,
                        content=todo.content,
                        created_at=todo.created_at,
                        updated_at=todo.updated_at,
                    ),
                    cursor=relay.to_base64(TodoType, todo.id),
                )
                for todo in paginated_result.entities
            ],
        )
