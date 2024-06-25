from typing import Annotated
from uuid import UUID

import strawberry
from aioinject import Inject
from aioinject.ext.strawberry import inject
from strawberry import relay

from .services import TodoService
from .types import TodoConnectionType


# TODO: add viewer type which returns todos maybe, so that we can use fragments easily in the client
@strawberry.type
class TodoQuery:
    @strawberry.field(
        graphql_type=TodoConnectionType,
    )
    @inject
    async def todos(
        self,
        todo_service: Annotated[TodoService, Inject],
        before: str | None = None,
        after: str | None = None,
        first: int | None = None,
        last: int | None = None,
    ) -> TodoConnectionType:
        paginated_result = await todo_service.get_all(
            limit=first or last,
            after=UUID(
                relay.from_base64(after)[-1],
            )
            if after
            else None,
            before=UUID(
                relay.from_base64(before)[-1],
            )
            if before
            else None,
        )

        return TodoConnectionType.from_paginated_result(
            paginated_result=paginated_result,
        )
