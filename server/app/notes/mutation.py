from typing import Annotated

import strawberry
from aioinject import Inject
from aioinject.ext.strawberry import inject

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
