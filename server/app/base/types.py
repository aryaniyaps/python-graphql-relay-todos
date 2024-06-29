from typing import Generic, Self, TypeVar

import strawberry
from strawberry import relay

from app.database.base import Base

ModelType = TypeVar("ModelType", bound=Base)


@strawberry.type
class BaseNodeType(Generic[ModelType], relay.Node):
    id: relay.NodeID[int]

    @classmethod
    def from_orm(cls, model: ModelType) -> Self:
        """Construct a node from an ORM instance."""
        raise NotImplementedError


@strawberry.interface(name="Error")
class BaseErrorType:
    message: str


NodeType = TypeVar("NodeType", bound=BaseNodeType[Base])
