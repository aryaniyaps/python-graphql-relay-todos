from datetime import datetime

import strawberry


@strawberry.type(name="Note")
class NoteType:
    id: str
    content: str
    created_at: datetime
    updated_at: datetime | None
