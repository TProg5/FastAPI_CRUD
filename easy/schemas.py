from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


class APIResponse(BaseModel):
    message: str
    user: User