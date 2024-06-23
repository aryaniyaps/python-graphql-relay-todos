from collections.abc import Iterable
from datetime import datetime
from typing import Self

import strawberry
from strawberry import relay
from strawberry.relay.types import NodeIterableType

from app.context import Info


@strawberry.type(name="Note")
class NoteType(relay.Node):
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
        return await info.context.loaders.note_by_id.load_many(node_ids)
