import os
import sys

from aerich.cli import coro
from config import settings
from db import init_db
from db.user import User

default_pass = "123456"


@coro
async def init_db_conn():
    await init_db()


@coro
async def init_user():
    user = await User.all().first()
    if not user:
        await User.create_user(username=settings.DEFAULT_USER, password=default_pass)


@coro
async def init_pass():
    user = await User.filter(user_name=settings.DEFAULT_USER).first()
    await user.reset_password(default_pass)


@coro
async def init_default_site_config():
    from db.config import SiteConfig, default_config

    configs = await SiteConfig.all()
    config_keys = [config.key for config in configs]
    not_in_db_config = []
    for key, value in default_config.items():
        if key not in config_keys:
            not_in_db_config.append(await SiteConfig.new(key=key, value=value))
    await SiteConfig.bulk_create(not_in_db_config)


def init_data_dir():
    from config import settings

    data_dir = os.path.join(settings.BASE_DIR, "data")
    palworld_dir = os.path.join(data_dir, "palworld")
    tmp_dir = os.path.join(data_dir, "tmp")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    if not os.path.exists(palworld_dir):
        os.makedirs(palworld_dir)
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)


if __name__ == "__main__":
    init_db_conn()
    init_data_dir()
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "reset_password":
            init_pass()
    else:
        init_user()
        init_default_site_config()
