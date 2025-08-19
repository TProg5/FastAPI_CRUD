from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    message: str
    user: User


class DeleteUserResponse(BaseModel):
    message: str
    user_id: int