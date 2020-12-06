from typing import List

from pydantic import Field
from pydantic.main import BaseModel


class Book(BaseModel):
    isbn: str
    title: str
    sub_title: str = Field(..., alias='subTitle')
    author: str
    publish_date: str
    publisher: str
    pages: str
    description: str
    website: str


class User(BaseModel):
    user_id: str = Field(..., alias='userId')
    username: str
    books: List[Book]


class TokenPayload(BaseModel):
    token: str = None
    expires: str = None
    status: str
    result: str