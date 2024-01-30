from fastapi import FastAPI, APIRouter, Depends
from fastapi.security import HTTPBearer

auth_schema = HTTPBearer(auto_error=False)
api_router = APIRouter(prefix="/api", dependencies=[Depends(auth_schema)])


def init(app: FastAPI):
    from .user import user_router
    from .player import player_router
    from .server import server_router

    api_router.include_router(user_router)
    api_router.include_router(player_router)
    api_router.include_router(server_router)

    app.include_router(api_router)
