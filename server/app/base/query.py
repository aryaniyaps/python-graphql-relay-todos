import strawberry
from strawberry import relay


@strawberry.type
class BaseQuery:
    node: relay.Node = relay.node()
