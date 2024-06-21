from sqlalchemy import delete, desc, select
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

    async def get(self, note_id: str) -> Note | None:
        """Get note by ID."""
        return await self._session.scalar(
            select(Note).where(
                Note.id == note_id,
            ),
        )

    async def get_all(self) -> list[Note]:
        """Get all notes."""
        statement = select(Note).order_by(desc(Note.created_at))

        scalars = await self._session.scalars(statement)

        return list(scalars)

    async def delete(self, note_id: str) -> None:
        """Delete a note by ID."""
        await self._session.execute(
            delete(Note).where(
                Note.id == note_id,
            ),
        )
        await self._session.commit()
