from sqlalchemy import select

from app.database.session import async_session_factory

from .models import Note


async def load_note_by_id(
    note_ids: list[str],
) -> list[Note | None]:
    stmt = select(Note).where(Note.id.in_(note_ids))

    async with async_session_factory() as session:
        note_by_id = {str(note.id): note for note in await session.scalars(stmt)}

    return [note_by_id.get(str(note_id)) for note_id in note_ids]
