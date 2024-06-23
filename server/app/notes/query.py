from typing import Annotated

import strawberry
from aioinject import Inject
from aioinject.ext.strawberry import inject
from strawberry import relay

from .services import NoteService
from .types import NoteType


@strawberry.type
class NoteQuery:
    @relay.connection(
        graphql_type=relay.ListConnection[NoteType],
    )
    @inject
    async def notes(
        self,
        note_service: Annotated[NoteService, Inject],
    ) -> list[NoteType]:
        notes = await note_service.get_all()

        return [
            NoteType(
                id=str(note.id),
                created_at=note.created_at,
                content=note.content,
                updated_at=note.updated_at,
            )
            for note in notes
        ]
