from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .context_request import add_context_request


def init(app: FastAPI) -> None:
    app.middleware("http")(add_context_request)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
