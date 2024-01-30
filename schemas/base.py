from datetime import datetime
from typing import Type, List, get_args, Self, Any

from pydantic import BaseModel, ConfigDict, Field


class ORMModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class BaseDbModel(ORMModel):
    id: int
    created_at: datetime
    updated_at: datetime


class PageSchema(BaseModel):
    total: int
    items: List[Type[ORMModel]]

    @classmethod
    async def from_queryset(cls, total, queryset) -> Self:
        items_anno = cls.__annotations__.get("items", BaseModel)
        model_class = get_args(items_anno)[0]
        items = []
        for item in queryset:
            items.append(model_class.from_orm(item))
        return cls(total=total, items=items)


class Success(BaseModel):
    show: bool = Field(default=True)
    detail: str

    def __init__(self, detail: str, **kwargs) -> None:
        kwargs["detail"] = detail
        super().__init__(**kwargs)
