from fastapi import FastAPI
from .init import scheduler, add_single_job, load_jobs


def init(app: FastAPI) -> None:
    @app.on_event("startup")
    async def startup() -> None:
        from db import init_db
        from .jobs import update_player, backup_palworld, restart_palworld_server

        await load_jobs()
        scheduler.start()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        scheduler.shutdown()
