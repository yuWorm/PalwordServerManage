from tortoise import fields

from db.base import BaseTable


class BroadCastMessage(BaseTable):
    message = fields.TextField(description="消息内容")

    @classmethod
    async def add(cls, msg):
        return await cls.create(message=msg)


class LogMessage(BaseTable):
    message = fields.TextField(description="日志消息")

    @classmethod
    async def new(cls, msg):
        return await cls.create(message=msg)
