from functools import lru_cache

import aioinject

from app.database.dependencies import get_session
from app.todos.repositories import TodoRepo
from app.todos.services import TodoService


@lru_cache
def create_container() -> aioinject.Container:
    container = aioinject.Container()
    container.register(aioinject.Scoped(get_session))
    container.register(aioinject.Scoped(TodoRepo))
    container.register(aioinject.Scoped(TodoService))

    return container
