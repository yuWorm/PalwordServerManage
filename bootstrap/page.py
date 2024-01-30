import os.path

from fastapi import FastAPI
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

from config import settings


def load_index_file():
    with open(os.path.join(settings.STATIC_FOLDER, "index.html"), "r") as f:
        return f.read()


html = load_index_file()


def init(app: FastAPI) -> None:
    app.mount("/static", StaticFiles(directory=settings.STATIC_FOLDER), name="static")

    @app.get("/")
    async def index():
        return HTMLResponse(html)
