from tortoise import Tortoise
from tortoise.contrib import fastapi
from fastapi import FastAPI
from .conf import tortoise_config


def init(app: FastAPI):
    fastapi.register_tortoise(
        app,
        config=tortoise_config,
    )


async def init_db():
    await Tortoise.init(config=tortoise_config)
