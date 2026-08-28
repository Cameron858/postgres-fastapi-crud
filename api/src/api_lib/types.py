from pydantic import BaseModel


class BaseItem(BaseModel):
    content: str


class ItemResponse(BaseItem):
    id: int
