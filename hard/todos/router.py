from typing import Annotated

from fastapi import APIRouter
from fastapi import HTTPException, Body
from hard.dependencies import DBConnect

from hard.todos.schemas import ToDo, ToDoResponse, ToDoResponseMessage
from hard.todos.repository import (
    create_todo, get_todo_by_id, 
    update_todo, delete_todo
)

todo = APIRouter(
    prefix="/api",
)


@todo.post("/todos/", response_model=ToDoResponse, status_code=201)
async def create_todo_endpoint(
    connection: DBConnect, 
    todo: Annotated[ToDo, Body()]
):  
    if todo.user_id <= 0:
        raise HTTPException(status_code=422, detail="user_id cannot be zero or a negative number")
     
    try:
        lastrowid = await create_todo(
            connection=connection,
            title=todo.title,
            description=todo.description, 
            completed=todo.completed,
            user_id=todo.user_id
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return ToDoResponse(
        message="ToDo successful created!",
        id=lastrowid,
        todo=ToDo(
            title=todo.title, 
            description=todo.description,
            completed=bool(todo.completed),
            user_id=todo.user_id
        )
    )
    

@todo.get("/todos/{todo_id}", response_model=ToDoResponse)
async def get_todo_endpoint(
    todo_id: int,
    connection: DBConnect
):
    try:
        row = await get_todo_by_id(
            connection=connection,
            todo_id=todo_id
        )
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    if not row:
        raise HTTPException(status_code=404, detail="Todo not Found")
    
    return ToDoResponse(
        id=todo_id,
        todo=ToDo(
            id=todo_id, 
            title=row["title"], 
            description=row["description"], 
            completed=bool(row["completed"]),
            user_id=row["user_id"]
        )
    )



@todo.put("/todos/{todo_id}", response_model=ToDoResponse)
async def update_todo_endpoint(
    connection: DBConnect,
    todo_id: int,
    todo: Annotated[ToDo, Body()]
):
    try:
        rowcount = await update_todo(
            connection=connection,
            todo_id=todo_id,
            title=todo.title,
            description=todo.description, 
            completed=todo.completed
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    if rowcount == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    return ToDoResponse(
        id=todo_id,
        todo=ToDo(
            id=todo_id, 
            title=todo.title, 
            description=todo.description, 
            completed=bool(todo.completed),
            user_id=todo.user_id
        )

    )

@todo.delete("/todos/{todo_id}")
async def delete_todo_endpoint(
    todo_id: int,
    connection: DBConnect
):
    try:
        todo_entity = await delete_todo(
            connection=connection,
            todo_id=todo_id
        )
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    if todo_entity == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    return ToDoResponseMessage(
        message=f"Todo with ID: {todo_id} deleted successfully"
    )