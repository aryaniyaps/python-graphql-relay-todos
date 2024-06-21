from .models import Note
from .repositories import NoteRepo


class NoteService:
    def __init__(self, note_repo: NoteRepo) -> None:
        self._note_repo = note_repo

    async def create_note(self, content: str) -> Note:
        """Create a new note."""
        return await self._note_repo.create(
            content=content,
        )

    async def get_all(self) -> list[Note]:
        """Get all notes."""
        return await self._note_repo.get_all()

    async def delete(self, note_id: str) -> Note:
        """Delete a note by ID."""
        existing_note = await self._note_repo.get(note_id=note_id)

        if existing_note is None:
            # TODO: raise NoteDoesNotExist error here
            raise Exception

        await self._note_repo.delete(
            note_id=note_id,
        )

        return existing_note
