from pydantic import BaseModel
from pydantic import field_validator
from fastapi.exceptions import HTTPException

class ToDo(BaseModel):
    title: str
    description: str
    completed: bool = False
    user_id: int | None = None

    @field_validator("user_id")
    @classmethod
    def validate_user_id(cls, value: int):
        if 0 >= value:
            raise HTTPException(status_code=422, detail="user_id cannot be zero or a negative number")


class ToDoResponseMessage(BaseModel):
    message: str


class ToDoResponse(BaseModel):
    message: str | None = None
    id: int
    todo: ToDo