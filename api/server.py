import json

from fastapi import APIRouter
from starlette.responses import StreamingResponse

from config import pal_settings
from db.config import SiteConfig
from scheduler.init import update_singe_job, remove_job
from scheduler.jobs import (
    update_player,
    restart_palworld_server,
    backup_palworld,
    update_palworld_server,
)
from schemas.base import Success
from schemas.config import IntervalConfigSchema
from schemas.enum import DockerStatusEnum
from schemas.server import ServerStatusSchema
from services import docker
from services import rcon
from schemas.palworld import PalGameWorldSettingsSchema
from services.auth import require_login

server_router = APIRouter(prefix="/server", tags=["服务器"])


@server_router.get("/pal/info", name="帕鲁服务器信息")
@require_login
async def get_pal_info():
    try:
        return await rcon.get_server_info()
    except Exception as e:
        return ""


@server_router.get("/info", name="运行信息")
# @require_login
async def server_info():
    status = await docker.server_status()
    if status != DockerStatusEnum.RUNNING:
        return {
            "memoryUsed": 0,
            "memoryTotal": 0,
            "memoryUsedPercent": 0,
            "cpuUsedPercent": 0,
            "cpuCount": 0,
            "networks": 0,
        }

    # info = await docker.palworld_runtime_info()
    return StreamingResponse(docker.palworld_runtime_info(), status_code=200)


@server_router.get("/status", name="服务器状态", response_model=ServerStatusSchema)
@require_login
async def server_status():
    status = await docker.server_status()
    return ServerStatusSchema(status=status)


@server_router.put("/restart", name="重启")
@require_login
async def server_restart():
    await docker.restart_palworld()
    return Success("重启成功")


@server_router.put("/start", name="启动")
@require_login
async def server_start():
    await docker.start_palworld()
    return Success("启动成功")


@server_router.put("/stop", name="停止")
@require_login
async def server_stop():
    await docker.stop_palworld()
    return Success("停止服务成功")


@server_router.post("/game_config", name="保存配置")
@require_login
async def server_config(config: PalGameWorldSettingsSchema, restart: bool = False):
    pal_settings.save_settings(json.loads(config.model_dump_json(by_alias=True)))
    if restart:
        await docker.restart_palworld()
        return Success("保存配置成功，已重启服务")

    return Success("保存配置成功，建议重启服务")


@server_router.get(
    "/game_config", name="获取配置", response_model=PalGameWorldSettingsSchema
)
@require_login
async def get_server_config():
    return PalGameWorldSettingsSchema(**pal_settings.settings)


@server_router.get("/interval", name="获取定时任务配置", response_model=IntervalConfigSchema)
async def update_interval_config():
    site_config = await SiteConfig.dict()
    return IntervalConfigSchema(**site_config)


@server_router.put("/interval", name="保存定时任务配置")
@require_login
async def update_interval_config(config: IntervalConfigSchema):
    site_config = await SiteConfig.dict()
    # 判断是否需要更新任务
    # 更新玩家数据
    if (
        config.update_player
        and config.update_player_interval != site_config["update_player_interval"]
    ):
        update_singe_job(
            update_player, "interval", seconds=config.update_player_interval
        )

    # 自动重启
    if (
        config.auto_restart_palworld_server
        and config.auto_restart_palworld_server_time
        != site_config["auto_restart_palworld_server_time"]
    ):
        update_singe_job(
            restart_palworld_server,
            "cron",
            minute=config.auto_restart_palworld_server_time.minute,
            hour=config.auto_restart_palworld_server_time.hour,
        )
    else:
        remove_job(restart_palworld_server)

    # 自动备份
    if (
        config.auto_backup
        and config.auto_backup_interval != site_config["auto_backup_interval"]
    ):
        update_singe_job(
            backup_palworld, trigger="interval", hours=config.auto_backup_interval
        )

    # 自动更新服务程序
    if (
        config.auto_update_palworld_server
        and config.auto_update_palworld_interval
        != site_config["auto_update_palworld_interval"]
    ):
        update_singe_job(
            update_palworld_server,
            trigger="interval",
            hours=config.auto_update_palworld_interval,
        )
    else:
        remove_job(update_palworld_server)

    # 循环判断是否需要更新数据库
    update_configs = {}
    config_dict = config.model_dump()
    for k, v in config_dict.items():
        if k in site_config and site_config[k] != v:
            update_configs[k] = v

    need_update_settings = await SiteConfig.filter(key__in=update_configs.keys()).all()

    for setting in need_update_settings:
        setting.value_str = str(update_configs[setting.key])

    await SiteConfig.bulk_update(need_update_settings, ["value_str"])
    return Success("保存成功，所有定时任务已更新")
