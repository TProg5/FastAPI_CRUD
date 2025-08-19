from typing import Annotated

from fastapi import APIRouter
from fastapi import HTTPException, Body
from middle.dependencies import DBConnect

from middle.schemas import ToDo, ToDoResponse

router = APIRouter(
    prefix="/api/v1"
)


@router.post("/todos/", response_model=ToDoResponse, status_code=201)
async def create_todo(
    connection: DBConnect, 
    todo: Annotated[ToDo, Body()]
):
    try:
        cursor = await connection.execute(
            """INSERT INTO todos (title, description, completed) VALUES (?, ?, ?)""",
            (todo.title, todo.description, todo.completed)
        )
        await connection.commit()
        todo_id = cursor.lastrowid

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return ToDoResponse(
        id=todo_id, 
        title=todo.title, 
        description=todo.description, 
        completed=bool(todo.completed)
    )
    

@router.get("/todos/{todo_id}", response_model=ToDoResponse)
async def get_todo(
    todo_id: int,
    connection: DBConnect
):
    try:
        cursor = await connection.execute(
            """SELECT * FROM todos WHERE id = ?""", (todo_id,)
        )

        todo = await cursor.fetchone()
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not Found")
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

    return ToDoResponse(
        id=todo_id, 
        title=todo["title"], 
        description=todo["description"], 
        completed=bool(todo["completed"])
    )



@router.put("/todos/{product_id}", response_model=ToDoResponse)
async def update_todo(
    connection: DBConnect,
    todo_id: int,
    todo: Annotated[ToDo, Body()]
):
    try:
        cursor = await connection.execute(
            """UPDATE todos SET title = ?, description = ?, completed = ? WHERE id = ?""",
            (todo.title, todo.description, todo.completed, todo_id)
        )

        await connection.commit()
        todo_id = cursor.lastrowid

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Todo not found")

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return ToDoResponse(id=todo_id, title=todo.title, description=todo.description, completed=bool(todo.completed))


@router.delete("/todos/{todo_id}")
async def delete_todo(
    todo_id: int,
    connection: DBConnect
):
    try:
        cursor = await connection.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
        await connection.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Todo not found")
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return {"detail": "Todo deleted successfully"}