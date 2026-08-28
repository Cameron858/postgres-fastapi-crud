from pydantic import BaseModel


class BaseItem(BaseModel):
    content: str


class ItemResponse(BaseItem):
    id: int


class ItemUpdate(BaseModel):
    id: int
    old_content: str
    new_content: str
