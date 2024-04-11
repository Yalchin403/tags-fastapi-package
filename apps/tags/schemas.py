from pydantic import BaseModel

from apps.tags.models import Tag


class TagSerializer(BaseModel):
    """
    Tag serializer

    Attributes:
        id (int): Tag id
        name (str): Tag name
    """

    id: int
    name: str

    class Config:
        orm_mode = True


class TagInSerializer(BaseModel):
    """
    Tag serializer

    Attributes:
        id (int): Tag id
        name (str): Tag name
    """

    name: str

    class Config:
        orm_mode = True
