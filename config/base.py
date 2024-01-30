import os
from pathlib import Path
from typing import Dict, Any
from .env import getenv, load_env
from .pal import PalGameSettings

BASE_DIR = Path(__file__).resolve().parent.parent

# 加载环境变量
load_env(BASE_DIR)


class LazyConfig:
    _data: Dict[str, Any] = {}

    def __init__(self):
        self._data = {}

    def __getattribute__(self, name):
        if name.startswith("_") or not name.isupper():
            return super().__getattribute__(name)
        if name not in self._data:
            # 获取配置数据类型，默认为str
            typehint = self.__annotations__.get(name, str)
            default = super().__getattribute__(name)
            self._data[name] = getenv(name, default, typehint)
        return self._data[name]

    def __getattr__(self, name):
        if name not in self.__annotations__.keys():
            return super().__getattribute__(name)

        return None


class BaseConfig(LazyConfig):
    BASE_DIR = Path(__file__).resolve().parent.parent
    ENV: str = getenv("ENV", "dev")
    DEBUG: bool = False
    SECRET_KEY: str = "dfh@()ADH@#UIFDHQH!@*#Yhdsh80sHWR!@"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 3600

    # 项目的一些信息
    PROJECT_NAME: str = "帕鲁服务器管理工具"
    PROJECT_DESCRIPTION: str = "帕鲁服务器管理工具"

    # 数据集配置
    DB_HOST: str = "127.0.0.1"
    DB_PORT: int = 3306
    DB_NAME: str = ""
    DB_ENGINE: str = "sqlite"
    DB_USER: str = "root"
    DB_PASSWORD: str = "123456"
    # sqlite 专用
    DB_FILE: str = "data/db.sqlite3"
    DEFAULT_USER: str = "palworld"

    # WEB配置
    WEB_HOST: str = "127.0.0.1"
    WEB_PORT: int = 8080
    WEB_DOMAIN: str = f"{WEB_HOST}:{WEB_PORT}"
    WEB_SCHEME: str = "http"

    # 静态资源配置
    STATIC_FOLDER: str = os.path.join(BASE_DIR, "static")

    # 帕鲁服务端的一些配置
    BACKUP_FOLDER: str = os.path.join(BASE_DIR, "data/backup")
    PALWORLD_CONTAINER_NAME: str = "steamcmd_palworld"
    RCON_PORT: int = 25575
    RCON_HOST: str = PALWORLD_CONTAINER_NAME
    PALWORLD_DATA_PATH: str = os.path.join(BASE_DIR, "data/palworld")
    PALWORLD_CONFIG_PATH: str = os.path.join(
        PALWORLD_DATA_PATH, "Pal/Saved/Config/LinuxServer/PalWorldSettings.ini"
    )
    PALWORLD_BLACKLIST_PATH: str = os.path.join(
        PALWORLD_DATA_PATH, "Pal/Saved/SaveGames/banlist.txt"
    )

    PALWORLD_GAME_DATA_PATH: str = os.path.join(PALWORLD_DATA_PATH, "Pal/Saved/")


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


class Config(BaseConfig):
    def __new__(cls, *args, **kwargs):
        config_cls = None
        if cls.ENV == "prod":
            config_cls = ProductionConfig
        elif cls.ENV == "dev":
            config_cls = DevelopmentConfig
        elif cls.ENV == "test":
            config_cls = TestingConfig
        else:
            config_cls = cls
        return config_cls(*args, **kwargs)
