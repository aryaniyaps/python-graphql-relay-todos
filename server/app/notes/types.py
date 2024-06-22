from datetime import datetime
from typing import Iterable

import strawberry
from strawberry import relay

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
    ):
        return await info.context.loaders.note_by_id.load_many(node_ids)
