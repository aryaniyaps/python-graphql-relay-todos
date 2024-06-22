import dataclasses

from fastapi import Request, Response, WebSocket
from strawberry.types import Info as StrawberryInfo

from app.dataloaders import Dataloaders


@dataclasses.dataclass
class Context:
    request: Request | WebSocket
    response: Response | None
    loaders: Dataloaders


Info = StrawberryInfo[Context, None]
