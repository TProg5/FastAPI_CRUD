from pydantic import BaseModel


class ToDo(BaseModel):
    title: str
    description: str
    completed: int = 0
    user_id: int | None = None

class ToDoResponseMessage(BaseModel):
    message: str

class ToDoResponse(BaseModel):
    message: str | None = None
    id: int
    todo: ToDo