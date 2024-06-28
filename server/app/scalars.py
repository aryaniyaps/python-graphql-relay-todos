import strawberry
from strawberry.relay import GlobalID

# temporary hack until strawberry fixes relay ID scalar generation
# https://github.com/strawberry-graphql/strawberry/issues/3551
ID = strawberry.scalar(
    strawberry.ID,
    serialize=lambda value: str(value),
    parse_value=lambda value: GlobalID.from_id(value=value),
)
