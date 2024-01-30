from config import settings


def make_connections():
    if settings.DB_ENGINE == "sqlite":
        return f"sqlite://{settings.DB_FILE}"
    elif settings.DB_ENGINE == "mysql":
        return {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": settings.DB_HOST,
                "port": settings.DB_PORT,
                "user": settings.DB_USER,
                "password": settings.DB_PASSWORD,
                "database": settings.DB_NAME,
            },
        }


tortoise_config = {
    "connections": {
        # Dict format for connection
        "default": make_connections()
    },
    "apps": {
        "models": {
            "models": ["db.models", "aerich.models"],
            # If no default_connection specified, defaults to 'default'
            "default_connection": "default",
        }
    },
}
