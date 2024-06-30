from typing import Annotated

import strawberry
from aioinject import Inject
from aioinject.ext.strawberry import inject
from strawberry import relay

from .repositories import TodoRepo
from .types import TodoConnectionType


@strawberry.type(name="Viewer")
class TodoQuery:
    @strawberry.field(  # type: ignore[misc]
        graphql_type=TodoConnectionType,
        description="Get all todos available.",
    )
    @inject
    async def todos(
        self,
        todo_repo: Annotated[TodoRepo, Inject],
        before: str | None = None,
        after: str | None = None,
        first: int | None = None,
        last: int | None = None,
    ) -> TodoConnectionType:
        paginated_result = await todo_repo.get_all(
            first=first,
            last=last,
            after=(
                int(
                    relay.from_base64(after)[1],
                )
                if after
                else None
            ),
            before=(
                int(
                    relay.from_base64(before)[1],
                )
                if before
                else None
            ),
        )

        return TodoConnectionType.from_paginated_result(
            paginated_result=paginated_result,
        )
