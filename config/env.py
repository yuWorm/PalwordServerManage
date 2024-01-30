import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

# 读取.env环境配置
ENV = os.getenv("ENV", "dev")


def load_env(base_dir: Path):
    """
    加载环境变量，将根目录传进去
    :param base_dir: 根目录
    """
    # 先读取.env，.env是通用的
    load_dotenv(os.path.join(base_dir, ".env"))
    # 根据环境变量读取对应的配置
    load_dotenv(os.path.join(base_dir, f".env.{ENV}"))
    local_env_path = os.path.join(base_dir, f".env.{ENV}.local")
    if os.path.exists(local_env_path):
        # 如果本地环境存在就加载本地环境
        load_dotenv(local_env_path, override=True)


def getenv(key, default=None, t=str) -> Any:
    """
    读取环境变量
    :param key: 环境变量的键值对
    :param default: 默认值
    :param t: 类型
    :return: 环境变量的值
    """
    value: str = os.getenv(key, default)
    if t == bool:
        if value.lower() == "false":
            return False
        else:
            return True

    return t(value)
