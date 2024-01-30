import json

import aiodocker.exceptions
from aiodocker import Docker, docker
from aiodocker.containers import DockerContainer
from fastapi import FastAPI

from config import settings
from exceptions.http import ContainerNotFoundError, DockerRuntimeError
from schemas.enum import DockerStatusEnum

client: Docker | None = None


def init(app: FastAPI) -> None:
    @app.on_event("startup")
    async def startup() -> None:
        await init_client()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        await close_client()


async def init_client():
    global client
    client = Docker()


async def close_client():
    await client.close()


def name(container: DockerContainer) -> str:
    names = container._container.get("Names")
    if len(names) == 0:
        return ""

    return names[0].replace("/", "")


def state(container):
    state_: str | dict = container._container.get("State")
    if type(state_) == str:
        return state_
    else:
        return state_.get("Status")


def status(container):
    return container._container.get("Status")


async def get_palworld_container() -> DockerContainer:
    try:
        return await client.containers.get(settings.PALWORLD_CONTAINER_NAME)
    except aiodocker.exceptions.DockerError as e:
        if e.status == 404:
            raise ContainerNotFoundError
        raise DockerRuntimeError(status_code=e.status, detail=e.message)


async def restart_palworld():
    """
    重启服务器
    :return:
    """
    container = await get_palworld_container()
    await container.restart()


async def stop_palworld():
    """
    重启服务器
    :return:
    """
    container = await get_palworld_container()
    await container.stop()


async def start_palworld():
    """
    重启服务器
    :return:
    """
    container = await get_palworld_container()
    await container.start()


async def palworld_runtime_info():
    """
    容器运行的信息
    :return:
    """
    container = await get_palworld_container()

    async for info in container.stats(stream=True):
        # 计算使用
        # 内存
        memory_stats = info.get("memory_stats", {})
        memory_used = memory_stats.get("usage", 0)
        memory_total = memory_stats.get("limit", 1)
        memory_used_percent = round((memory_used / memory_total) * 100, 2)
        # CPU
        cpu_stats = info.get("cpu_stats", {})
        cpu_count = cpu_stats.get("online_cpus", 0)
        cpu_used = cpu_stats.get("cpu_usage", {}).get("total_usage", 0)
        cpu_total = cpu_stats.get("system_cpu_usage")
        cpu_used_percent = round((cpu_used / cpu_total) * 100, 2)

        # network

        network_stats = info.get("networks", {})

        stats = {
            "memoryUsed": memory_used,
            "memoryTotal": memory_total,
            "memoryUsedPercent": memory_used_percent,
            "cpuUsedPercent": cpu_used_percent,
            "cpuCount": cpu_count,
            "networks": network_stats,
            "cpuStats": cpu_stats,
        }

        yield json.dumps(stats)


async def server_status():
    container = await get_palworld_container()
    return state(container)


async def update_palworld_server():
    container = await get_palworld_container()
    exec_obj = await container.exec(
        "bash -c /home/steam/steamcmd/steamcmd.sh +login anonymous +app\_update 2394010 validate +quit",
        stdout=True,
    )

    stream = exec_obj.start(timeout=60 * 60)
    while True:
        msg = await stream.read_out()
        if msg is None:
            break
        data = msg.data.decode("utf-8")
        yield data
