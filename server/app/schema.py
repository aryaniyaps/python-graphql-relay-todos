from aioinject.ext.strawberry import AioInjectExtension
from strawberry import Schema
from strawberry.extensions import ParserCache, ValidationCache
from strawberry.relay import GlobalID
from strawberry.tools import merge_types

from app.scalars import ID

from .base.query import BaseQuery
from .container import create_container
from .todos.mutation import TodoMutation
from .todos.query import TodoQuery

query = merge_types(
    name="Query",
    types=(
        BaseQuery,
        TodoQuery,
    ),
)


mutation = merge_types(
    name="Mutation",
    types=(TodoMutation,),
)


schema = Schema(
    query=query,
    mutation=mutation,
    extensions=[
        AioInjectExtension(
            container=create_container(),
        ),
        ParserCache(maxsize=128),
        ValidationCache(maxsize=128),
    ],
    scalar_overrides={GlobalID: ID},
)
