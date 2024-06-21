import strawberry


@strawberry.type(name="Note")
class NoteType:
    content: str
