import logging
import os
from datetime import datetime

from config import settings
from db.message import LogMessage
from services import rcon, docker
from utils.file import zip_file
from db import init_db

logger = logging.getLogger("定时任务")

is_init_db = False


def use_db(func):
    async def wrapper(*args, **kwargs):
        global is_init_db

        if not is_init_db:
            await init_db()
            is_init_db = True
        return await func(*args, **kwargs)

    return wrapper


@use_db
async def backup_palworld():
    from db.message import LogMessage

    today = datetime.today()
    date_str = today.strftime("%Y-%m-%d-%H")

    target_file = os.path.join(settings.BACKUP_FOLDER, f"{date_str}.zip")

    zip_file(settings.PALWORLD_GAME_DATA_PATH, target_file)
    await LogMessage.new(f"备份完成，路径：{target_file}")
    logger.info(f"备份完成")


@use_db
async def update_player():
    try:
        online_player = await rcon.get_players()
    except Exception as e:
        logger.error(e)


@use_db
async def restart_palworld_server():
    await docker.restart_palworld()
    await LogMessage.new("执行重启完成")


@use_db
async def update_palworld_server():
    infos = ""
    async for info in docker.update_palworld_server():
        infos += info
    await LogMessage.new(f"执行更新完毕,更新返回的信息：{infos}")
