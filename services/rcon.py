import asyncio
import csv
from io import StringIO

from gamercon_async import GameRCON
from config import settings, pal_settings
from exceptions.http import RCONTimeoutError, RCONSettingError


async def sen_command(command: str, message: str = "") -> str:
    """
    发送命令
    :param command: 命令名
    :param message: 参数
    :return: 结果
    """
    rcon_enable = pal_settings.get("RCONEnabled")
    if not rcon_enable:
        raise RCONSettingError("请先开启RCON服务，才可使用此功能")
    rcon_port = pal_settings.get("RCONPort")
    if not rcon_port:
        raise RCONSettingError("请先开启RCON服务并设置RCON端口，才可使用此功能")
    password = pal_settings.get("AdminPassword")
    if not password:
        raise RCONSettingError("请先设置管理员密码，才可使用此功能")

    try:
        async with GameRCON(
            host=settings.RCON_HOST,
            port=settings.RCON_PORT,
            password=pal_settings.get("AdminPassword"),
        ) as client:
            return await client.send(f"{command} {message}")
    except asyncio.TimeoutError:
        raise RCONTimeoutError


async def broadcast(message):
    from db.message import BroadCastMessage

    result = await sen_command("Broadcast", message)
    if result.startswith("Broadcasted"):
        await BroadCastMessage.add(message)


async def get_players():
    """
    获取在线的用户
    :return:
    """
    from db.user import Player

    players_str: str = await sen_command("ShowPlayers")
    sio = StringIO(players_str)
    csvreader = csv.DictReader(sio)
    not_in_db_players = []
    online_player_dict = {}
    for row in csvreader:
        online_player_dict[row["steamid"]] = row
    players = await Player.filter(steamid__in=online_player_dict.keys()).all()
    in_db_players = []
    for player in players:
        in_db_players.append(player.steamid)
        player.online = True

    for steamid, value in online_player_dict.items():
        if steamid not in in_db_players:
            not_in_db_players.append(Player(online=True, **value))

    await Player.bulk_create(not_in_db_players)
    await Player.bulk_update(players, ["online"])
    return players + not_in_db_players


async def get_server_info():
    return await sen_command("Info")
