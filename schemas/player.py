from typing import List

from .base import BaseDbModel, PageSchema


class PlayerSchema(BaseDbModel):
    name: str
    steamid: str
    playeruid: str


class PlayerPageSchema(PageSchema):
    items: List[PlayerSchema]
