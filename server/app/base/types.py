from typing import Any, Self, TypeVar

import strawberry
from strawberry import relay
from strawberry.relay.types import NodeIterableType

from app.context import Info
from app.database.paginator import PaginatedResult

NodeT = TypeVar(
    "NodeT",
    bound=relay.Node,
)


# class KeysetConnection(relay.Connection):
#     @classmethod
#     async def resolve_connection(
#         cls,
#         nodes: NodeIterableType[NodeT],
#         *,
#         info: Info,
#         before: str | None = None,
#         after: str | None = None,
#         first: int | None = None,
#         last: int | None = None,
#         **kwargs: Any,
#     ) -> Self:
#         # NOTE: This is a showcase implementation and is far from
#         # being optimal performance wise
#         edges_mapping = {
#             relay.to_base64("fruit_name", n.name): relay.Edge(
#                 node=n,
#                 cursor=relay.to_base64("fruit_name", n.name),
#             )
#             for n in sorted(nodes, key=lambda f: f.name)
#         }
#         edges = list(edges_mapping.values())
#         first_edge = edges[0] if edges else None
#         last_edge = edges[-1] if edges else None

#         if after is not None:
#             after_edge_idx = edges.index(edges_mapping[after])
#             edges = [e for e in edges if edges.index(e) > after_edge_idx]

#         if before is not None:
#             before_edge_idx = edges.index(edges_mapping[before])
#             edges = [e for e in edges if edges.index(e) < before_edge_idx]

#         if first is not None:
#             edges = edges[:first]

#         if last is not None:
#             edges = edges[-last:]

#         return cls(
#             edges=edges,
#             page_info=relay.PageInfo(
#                 start_cursor=edges[0].cursor if edges else None,
#                 end_cursor=edges[-1].cursor if edges else None,
#                 has_previous_page=(
#                     first_edge is not None and bool(edges) and edges[0] != first_edge
#                 ),
#                 has_next_page=(
#                     last_edge is not None and bool(edges) and edges[-1] != last_edge
#                 ),
#             ),
#         )


@strawberry.type
class BaseConnectionType(relay.Connection[NodeT]):
    @classmethod
    def from_paginated_result(cls, paginated_result: PaginatedResult) -> Self:
        """Construct a connection from a paginated result object."""
        return cls(
            page_info=relay.PageInfo(
                has_next_page=paginated_result.page_info.has_next_page,
                start_cursor=relay.to_base64(
                    NodeT,
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
                    cursor=relay.to_base64(NodeT, todo.id),
                )
                for todo in paginated_result.entities
            ],
        )
