from pydantic import BaseModel
from hard.todos.schemas import ToDoResponse


class TodoWithUserResponse(BaseModel):
    user_id: int
    username: str
    todo: ToDoResponse