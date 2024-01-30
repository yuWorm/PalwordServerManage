import uvicorn

from config import settings


def upgrade_database():
    pass


def run():
    uvicorn.run(
        "bootstrap.app:application",
        host=settings.WEB_HOST,
        port=settings.WEB_PORT,
        log_level="debug" if settings.DEBUG else "info",
        reload=settings.DEBUG,
        reload_excludes=["static", "templates"],
    )
