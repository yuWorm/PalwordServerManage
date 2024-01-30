import datetime

from apscheduler.jobstores.base import JobLookupError

from db.config import SiteConfig
from .jobs import update_player

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()


def add_single_job(func, *args, **kwargs):
    if scheduler.get_job(func.__name__):
        return
    scheduler.add_job(func, *args, id=func.__name__, **kwargs)


def update_singe_job(func, *args, **kwargs):
    if scheduler.get_job(func.__name__):
        scheduler.remove_job(func.__name__)
    else:
        scheduler.add_job(func, *args, **kwargs, id=func.__name__)


def remove_job(func, *args, **kwargs):
    if scheduler.get_job(func.__name__):
        scheduler.remove_job(func.__name__)


async def load_jobs():
    from .jobs import (
        backup_palworld,
        restart_palworld_server,
        update_palworld_server,
        update_player,
    )

    site_config = await SiteConfig.dict()

    auto_backup = site_config.get("auto_backup")
    if auto_backup:
        auto_backup_interval = site_config.get("auto_backup_interval")
        add_single_job(backup_palworld, trigger="interval", hours=auto_backup_interval)

    auto_restart_palworld_server = site_config.get("auto_restart_palworld_server")
    if auto_restart_palworld_server:
        auto_restart_palworld_server_time: datetime.datetime = site_config.get(
            "auto_restart_palworld_server_time"
        )
        add_single_job(
            restart_palworld_server,
            "cron",
            minute=auto_restart_palworld_server_time.minute,
            hour=auto_restart_palworld_server_time.hour,
        )

    auto_update_palworld_server = site_config.get("auto_update_palworld_server")
    if auto_update_palworld_server:
        auto_update_palworld_interval: int = site_config.get(
            "auto_update_palworld_interval"
        )
        add_single_job(
            update_palworld_server,
            trigger="interval",
            hours=auto_update_palworld_interval,
        )

    enable_update_player = site_config.get("update_player")
    if enable_update_player:
        update_player_interval: int = site_config.get("update_player_interval")
        add_single_job(
            update_player, trigger="interval", seconds=update_player_interval
        )
