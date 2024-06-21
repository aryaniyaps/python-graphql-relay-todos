from typing import Annotated

import strawberry
from aioinject import Inject, inject

from .models import Note
from .services import NoteService
from .types import NoteType


@strawberry.type
class NoteQuery:
    @strawberry.field(
        graphql_type=list[NoteType],
        description="Get all notes.",
    )
    @inject
    async def all_notes(
        self, note_service: Annotated[NoteService, Inject]
    ) -> list[Note]:
        """Get all notes."""
        return await note_service.get_all()
