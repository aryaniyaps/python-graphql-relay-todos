from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from .config import settings
from .schema import schema


def add_routes(app: FastAPI) -> None:
    """Register routes for the app."""
    app.include_router(
        GraphQLRouter(
            schema=schema,
        ),  # type: ignore
        prefix="/graphql",
    )


def add_middleware(app: FastAPI) -> None:
    """Register middleware for the app."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_allow_origins,
        allow_credentials=True,
        allow_headers=["*"],
        allow_methods=["*"],
        expose_headers=["*"],
    )


def create_app() -> FastAPI:
    app = FastAPI(
        version="0.0.1",
        debug=settings.debug,
        openapi_url=settings.openapi_url,
    )
    add_routes(app)
    add_middleware(app)
    return app
