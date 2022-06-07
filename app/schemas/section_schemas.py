import email
from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel
from app.schemas.item_schemas import ItemSchema

T = TypeVar('T')


class SectionSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    items:Optional[List[ItemSchema]]= None

    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestSection(BaseModel):
    parameter: SectionSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
