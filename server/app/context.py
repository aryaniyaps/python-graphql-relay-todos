import dataclasses

from starlette.requests import Request
from starlette.responses import Response
from starlette.websockets import WebSocket
from strawberry.types import Info as StrawberryInfo

from app.dataloaders import Dataloaders


@dataclasses.dataclass
class Context:
    request: Request | WebSocket
    response: Response | None
    loaders: Dataloaders


Info = StrawberryInfo[Context, None]
