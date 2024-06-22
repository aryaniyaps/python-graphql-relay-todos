from typing import Annotated

import strawberry
from aioinject import Inject
from aioinject.ext.strawberry import inject
from strawberry import relay

from app.context import Info

from .models import Note
from .services import NoteService
from .types import NoteType


@strawberry.type
class NoteMutation:
    @strawberry.mutation(
        graphql_type=NoteType,
        description="Create a new note.",
    )
    @inject
    async def create_note(
        self,
        content: Annotated[
            str,
            strawberry.argument(
                description="The content of the note.",
            ),
        ],
        note_service: Annotated[NoteService, Inject],
    ) -> Note:
        """Create a new note."""
        return await note_service.create_note(
            content=content,
        )

    @strawberry.mutation(
        graphql_type=None,
        description="Delete a note by ID.",
    )
    @inject
    async def delete_note(
        self,
        info: Info,
        note_id: Annotated[
            relay.GlobalID,
            strawberry.argument(
                description="The ID of the note to delete.",
            ),
        ],
        note_service: Annotated[NoteService, Inject],
    ) -> None:
        """Delete a note by ID."""
        note = await note_id.resolve_node(info, ensure_type=NoteType)
        await note_service.delete(note_id=note.id)
