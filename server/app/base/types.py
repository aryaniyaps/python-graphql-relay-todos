from typing import (
    Annotated,
    Any,
    AsyncIterable,
    AsyncIterator,
    Iterable,
    Iterator,
    List,
    Optional,
    TypeVar,
)

import strawberry
from aioinject import Inject
from aioinject.ext.strawberry import inject
from sqlakeyset import Page, unserialize_bookmark
from sqlakeyset.asyncio import select_page
from sqlalchemy.ext.asyncio import AsyncSession
from strawberry import relay

from app.context import Info

T = TypeVar("T", bound=relay.Node)


@strawberry.type(name="Connection", description="A connection to a list of items.")
class KeysetConnection(relay.Connection[T]):
    edges: List[relay.Edge[T]] = strawberry.field(
        description="Contains the nodes in this connection",
    )

    @classmethod
    @inject
    async def resolve_connection(
        cls,
        nodes: Iterator[T] | Iterable[T] | AsyncIterator[T] | AsyncIterable[T],
        *,
        info: Info,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        session: Annotated[AsyncSession, Inject],
        **kwargs: Any,
    ) -> "KeysetConnection[T]":
        if first is not None and last is not None:
            raise ValueError("Cannot specify both first and last")

        max_results = info.schema.config.relay_max_results
        per_page = first or last or max_results

        if per_page > max_results:
            raise ValueError(f"Cannot request more than {max_results} results")

        # Use sqlakeyset to paginate
        page: Page = await select_page(
            session,
            nodes,
            per_page=per_page,
            after=unserialize_bookmark(after) if after else None,
            before=unserialize_bookmark(before) if before else None,
        )

        # Create edges
        # (Overriding Edge.resolve_edge as we already have base64 encoded cursors from
        # sqlakeyset available!)
        edges = [
            relay.Edge(node=node, cursor=page.paging.get_bookmark_at(i))
            for i, node in enumerate(page)
        ]

        return cls(
            edges=edges,
            page_info=relay.PageInfo(
                has_next_page=page.paging.has_next,
                has_previous_page=page.paging.has_previous,
                start_cursor=page.paging.get_bookmark_at(0) if page else None,
                end_cursor=page.paging.get_bookmark_at(-1) if page else None,
            ),
        )
