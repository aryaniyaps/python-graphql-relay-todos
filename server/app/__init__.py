from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .graphql_app import create_graphql_app


def add_routes(app: FastAPI) -> None:
    """Register routes for the app."""
    app.mount("/graphql", create_graphql_app())


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
