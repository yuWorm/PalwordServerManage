from tortoise import fields

from config import pal_settings
from .base import BaseTable
from typing import Tuple, Type, Self
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def make_password(password: str) -> str:
    """
    加密密码
    :param password: 明文密码
    :return: 密文
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    校验密码
    :param plain_password: 明文密码
    :param hashed_password: 密文密码
    :return: 是否正确
    """
    return pwd_context.verify(plain_password, hashed_password)


class User(BaseTable):
    username = fields.CharField(max_length=20, unique=True, description="用户名")
    password = fields.CharField(max_length=256, description="用户密码")

    @classmethod
    async def _create_user(cls, username: str, password: str):
        """
        创建用户
        :param username: 用户名
        :param password: 用户密码
        :return: 用户对象
        """
        en_password = make_password(password)
        return await cls.create(
            username=username,
            password=en_password,
        )

    @classmethod
    async def create_user(cls, username: str, password: str):
        """
        创建普通用户
        :param username: 用户名
        :param password: 用户密码
        :return: 用户对象
        """
        return await cls._create_user(username, password)

    async def reset_password(self, plain_password: str):
        self.password = make_password(plain_password)
        await self.save()

    def verify(self, password) -> bool:
        """
        检查密码
        :param password: 密码明文
        :return: 密码是否正确
        """
        return verify_password(password, self.password)

    @classmethod
    async def authenticate(cls, username, password) -> None | Type[Self]:
        user = await cls.filter(username=username).first()
        if not user:
            return None
        if not user.verify(password):
            return None
        return user

    class Meta:
        table_name = "user"


class Player(BaseTable):
    name = fields.CharField(max_length=256, description="玩家名称")
    playeruid = fields.CharField(max_length=256, description="玩家ID")
    steamid = fields.CharField(max_length=256, description="玩家的SteamID")
    online = fields.BooleanField(default=False, description="玩家是否在线")

    class Meta:
        table_name = "player"

    @property
    def in_blacklist(self) -> bool:
        return pal_settings.in_blacklist(self.steamid)
