from typing import Annotated

import strawberry
from aioinject import Inject
from aioinject.ext.strawberry import inject
from strawberry import relay

from app.base.types import KeysetConnection

from .models import Note
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
    ) -> list[Note]:
        return await note_service.get_all()
