from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Note


class NoteRepo:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, content: str) -> Note:
        """Create a new note."""
        note = Note(content=content)
        self._session.add(note)
        await self._session.commit()
        return note

    async def get_all(self) -> list[Note]:
        """Get all notes."""
        statement = select(Note).order_by(desc(Note.created_at))

        scalars = await self._session.scalars(statement)

        return list(scalars)
