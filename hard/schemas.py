from typing import List
from pydantic import BaseModel


class TodoItem(BaseModel):
    todo_id: int
    title: str
    description: str
    completed: int


class TodoWithUserResponse(BaseModel):
    user_id: int
    username: str
    todo: List[TodoItem]
