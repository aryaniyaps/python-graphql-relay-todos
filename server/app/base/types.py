from typing import Any, Generic, Self, TypeVar

import strawberry
from strawberry import relay
from strawberry.utils.await_maybe import AwaitableOrValue

from app.context import Info
from app.database.paginator import CursorType, ModelType, PaginatedResult


@strawberry.type
class BaseNodeType(Generic[ModelType], relay.Node):
    id: relay.NodeID[int]

    @classmethod
    def from_orm(cls, model: ModelType) -> Self:
        """Construct a node from an ORM instance."""
        raise NotImplementedError


NodeType = TypeVar("NodeType", bound=BaseNodeType)


@strawberry.type
class PaginatedResultConnection(
    Generic[NodeType, ModelType, CursorType],
    relay.Connection[NodeType],
):
    @classmethod
    def resolve_connection(
        cls,
        paginated_result: PaginatedResult[ModelType, CursorType],  # type: ignore[override]
        *,
        info: Info,
        before: str | None = None,
        after: str | None = None,
        first: int | None = None,
        last: int | None = None,
        **kwargs: Any,
    ) -> AwaitableOrValue[Self]:
        return cls(
            page_info=relay.PageInfo(
                has_next_page=paginated_result.page_info.has_next_page,
                start_cursor=relay.to_base64(
                    NodeType,
                    paginated_result.page_info.start_cursor,
                ),
                has_previous_page=paginated_result.page_info.has_previous_page,
                end_cursor=relay.to_base64(
                    NodeType,
                    paginated_result.page_info.end_cursor,
                ),
            ),
            edges=[
                relay.Edge(
                    node=NodeType.from_orm(entity),
                    cursor=relay.to_base64(NodeType, entity.id),
                )
                for entity in paginated_result.entities
            ],
        )

    @classmethod
    def from_paginated_result(cls, paginated_result: PaginatedResult) -> Self:
        return cls(
            page_info=relay.PageInfo(
                has_next_page=paginated_result.page_info.has_next_page,
                start_cursor=relay.to_base64(
                    NodeType,
                    paginated_result.page_info.start_cursor,
                ),
                has_previous_page=paginated_result.page_info.has_previous_page,
                end_cursor=relay.to_base64(
                    NodeType,
                    paginated_result.page_info.end_cursor,
                ),
            ),
            edges=[
                relay.Edge(
                    node=NodeType.from_orm(entity),
                    cursor=relay.to_base64(NodeType, entity.id),
                )
                for entity in paginated_result.entities
            ],
        )
