from pydantic import BaseModel
from typing import Optional


class UserCreateBody(BaseModel):
    username: str
    password: str
    email: str


class NewServerBody(BaseModel):
    name: str


class NewMessageBody(BaseModel):
    server_id: str
    message_content: str


class UserBody(BaseModel):
    uid: str
    password: str
