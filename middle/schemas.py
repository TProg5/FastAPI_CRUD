from pydantic import BaseModel


class ToDo(BaseModel):
    title: str
    description: str
    completed: int = 0


class ToDoResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool