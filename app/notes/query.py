import strawberry

from .types import NoteType


@strawberry.type
class NoteQuery:
    @strawberry.field
    async def get_all_notes(
        self,
    ) -> list[NoteType]:
        raise NotImplementedError
