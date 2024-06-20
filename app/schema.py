from strawberry import Schema
from strawberry.extensions import ParserCache, ValidationCache
from strawberry.tools import merge_types

from .notes.mutation import NoteMutation
from .notes.query import NoteQuery

query = merge_types(
    name="Query",
    types=(NoteQuery,),
)


mutation = merge_types(
    name="Mutation",
    types=(NoteMutation,),
)


schema = Schema(
    query=query,
    mutation=mutation,
    extensions=[
        ParserCache(maxsize=128),
        ValidationCache(maxsize=128),
    ],
)
