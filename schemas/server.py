from pydantic import BaseModel

from schemas.enum import DockerStatusEnum


class ServerStatusSchema(BaseModel):
    status: DockerStatusEnum
