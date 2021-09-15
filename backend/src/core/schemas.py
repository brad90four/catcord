from pydantic import BaseModel
from typing import Optional


class UserCreateBody(BaseModel):
    username: str
    password: str
    email: str
    phone: str
    avatar: Optional[str] = None


class NewServerBody(BaseModel):
    name: str


class NewMessageBody(BaseModel):
    server_id: str
    message_content: str


class UserBody(BaseModel):
    uid: str
    password: str
