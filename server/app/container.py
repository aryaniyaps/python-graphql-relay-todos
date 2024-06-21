from functools import lru_cache

import aioinject

from app.database.dependencies import get_session
from app.notes.repositories import NoteRepo
from app.notes.services import NoteService


@lru_cache
def create_container() -> aioinject.Container:
    container = aioinject.Container()
    container.register(aioinject.Scoped(get_session))
    container.register(aioinject.Scoped(NoteRepo))
    container.register(aioinject.Scoped(NoteService))

    return container
