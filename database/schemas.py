from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: Optional[str] = None


class UserAuth(UserBase):
    password: str


class UserUpdate(UserAuth):
    new_password: Optional[str] = None


class ShortLinkBase(BaseModel):
    route: str


class ShortLinkBaseWithAuth(UserAuth):
    route: str


class ShortLinkCreate(ShortLinkBaseWithAuth):
    url: str


class ShortLinkUpdate(ShortLinkCreate):
    new_url: Optional[str] = None
    new_route: Optional[str] = None
