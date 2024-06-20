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

    async def get_all_notes(self) -> list[Note]:
        """Get all notes."""
        return await self._note_repo.get_all()
