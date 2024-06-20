import strawberry

from .types import NoteType


@strawberry.type
class NoteMutation:
    @strawberry.mutation
    async def create_note(
        self,
        content: str,
    ) -> NoteType:
        raise NotImplementedError
