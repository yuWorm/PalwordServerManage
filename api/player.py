from fastapi import APIRouter

from schemas.player import PlayerPageSchema, PlayerSchema
from services import rcon

player_router = APIRouter(prefix="/player", tags=["玩家"])


@player_router.get("/online/list", name="在线玩家列表")
async def online_player_list():
    return await rcon.get_server_info()


@player_router.get("/all/list", name="所有玩家列表", response_model=PlayerPageSchema)
async def all_player_list():
    players = await rcon.get_players()
    return PlayerPageSchema(
        total=len(players), items=[PlayerSchema.from_orm(player) for player in players]
    )


@player_router.get("/blacklist", name="黑名单")
async def blacklist():
    pass


@player_router.delete("/unblack/{steamid}", name="将玩家移除黑名单")
async def unblack_player():
    pass


@player_router.post("/ban/{steamid}", name="将玩家加入黑名单")
async def ban_player(steamid: str):
    pass


@player_router.post("/kick/{steamid}", name="将玩家踢出服务器")
async def kick_player(steamid: str):
    pass


@player_router.post("/broadcast", name="广播消息")
async def broadcast():
    pass
