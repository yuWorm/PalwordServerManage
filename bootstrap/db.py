import os

from aerich import Migrate
from aerich.cli import coro


@coro
async def init_db():
    from aerich import Command
    from config import settings

    from db.conf import tortoise_config

    command = Command(
        tortoise_config=tortoise_config,
        app="models",
        location=os.path.join(settings.BASE_DIR, "db/migrations"),
    )
    await command.init()

    await command.init_db(True)


def init():
    from config import settings

    migrations_dir = os.path.join(settings.BASE_DIR, "db/migrations")
    migrate_list = os.listdir(migrations_dir)
    if len(migrate_list) == 0:
        init_db()
