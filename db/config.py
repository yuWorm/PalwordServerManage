from datetime import datetime
from typing import Self

from .base import BaseTable
from tortoise import fields
from utils.type import BASE_TYPE, translate_type


default_config = {
    "auto_restart_palworld_server": False,
    "auto_restart_palworld_server_time": datetime.now(),
    "auto_backup": False,
    "auto_backup_interval": 0,
    "update_player": True,
    "update_player_interval": 20,
    "auto_update_palworld_server": False,
    "auto_update_palworld_interval": datetime.now(),
}


class SiteConfig(BaseTable):
    """
    一些配置，主要用于定时任务的一些配置
    """

    key = fields.CharField(max_length=100, description="配置名称", unique=True)
    value_str = fields.CharField(max_length=255, description="配置值")
    type = fields.CharField(max_length=100, description="值的类型")

    @classmethod
    async def set(cls, key, value) -> Self:
        t = type(value).__name__.lower()
        if t not in BASE_TYPE.keys():
            raise ValueError(f"不支持的类型")

        # 有存无加
        obj = await cls.filter(key=key).first()
        if obj:
            obj.value_str = f"{value}"
            await obj.save()
            return obj

        return await cls.create(key=key, value_str=f"{value}", type=t)

    @classmethod
    async def value(cls, key) -> int | str | datetime | float | bool:
        config = await cls.filter(key=key).first()
        return config.value_

    @property
    def value_(self):
        if not self.value_str:
            raise None

        return translate_type(self.value_str, self.type)

    @classmethod
    async def new(cls, key, value) -> Self:
        t = type(value).__name__.lower()
        if t not in BASE_TYPE.keys():
            raise ValueError(f"不支持的类型")

        return cls(key=key, value_str=f"{value}", type=t)

    @classmethod
    async def dict(cls) -> dict:
        result = {}
        configs = await cls.all()
        for config in configs:
            result[config.key] = config.value_
        return result
