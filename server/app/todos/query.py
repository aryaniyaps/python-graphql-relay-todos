from typing import Annotated

import strawberry
from aioinject import Inject
from aioinject.ext.strawberry import inject
from strawberry import relay

from .services import TodoService
from .types import TodoConnectionType


# TODO: add viewer type which returns todos maybe, so that we can use fragments easily in the client
@strawberry.type
class TodoQuery:
    @relay.connection(
        graphql_type=TodoConnectionType,
    )
    @inject
    async def todos(
        self,
        todo_service: Annotated[TodoService, Inject],
    ) -> TodoConnectionType:
        # TODO: find a way to get limit, after and before here
        # TODO: find a way to base64 decode cursors here
        paginated_result = await todo_service.get_all(
            limit=limit,
            after=after,
            before=before,
        )

        return TodoConnectionType.from_paginated_result(
            paginated_result=paginated_result,
        )
