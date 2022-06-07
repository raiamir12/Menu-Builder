import email
from random import choices
from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel
from app.schemas.modifier_schemas import ModifierSchema

T = TypeVar('T')


class ItemSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None
    choices:Optional[list[ModifierSchema]]=None

    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestItem(BaseModel):
    parameter: ItemSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
