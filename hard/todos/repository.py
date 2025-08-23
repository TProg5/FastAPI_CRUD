from typing import Optional
from hard.dependencies import DBConnect
import aiosqlite

async def create_todo(
    connection: DBConnect, 
    title: str, 
    description: str, 
    user_id: int,
    completed: int = 0,
) -> int:
    cursor = await connection.execute(
        "INSERT INTO todos (title, description, completed, user_id) VALUES (?, ?, ?, ?)",
        (title, description, completed, user_id)
    )
    await connection.commit()
    return cursor.lastrowid


async def get_todo_by_id(
    connection: DBConnect, 
    todo_id: int
) -> Optional[aiosqlite.Row]:
    cursor = await connection.execute(
        "SELECT * FROM todos WHERE id = ?", 
        (todo_id,)
    )
    return await cursor.fetchone()


async def update_todo(
    connection: DBConnect, 
    todo_id: int, 
    title: str, 
    description: str, 
    completed: int
) -> int:
    cursor = await connection.execute(
        "UPDATE todos SET title = ?, description = ?, completed = ? WHERE id = ?",
        (title, description, completed, todo_id)
    )
    await connection.commit()
    return cursor.rowcount


async def delete_todo(
    connection: DBConnect, 
    todo_id: int
) -> int:
    cursor = await connection.execute(
        "DELETE FROM todos WHERE id = ?", 
        (todo_id,)
    )
    await connection.commit()
    return cursor.rowcount
