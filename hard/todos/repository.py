from typing import Optional
from hard.dependencies import DBConnect
import aiosqlite

# Создать новый Todo
async def create_todo(
    connection: DBConnect, 
    title: str, 
    description: str, 
    user_id: int,
    completed: int = 0,
) -> int:
    """
    Возвращает ID созданного Todo.
    """
    cursor = await connection.execute(
        "INSERT INTO todos (title, description, completed, user_id) VALUES (?, ?, ?, ?)",
        (title, description, completed, user_id)
    )
    await connection.commit()
    return cursor.lastrowid

# Получить Todo по id
async def get_todo_by_id(
    connection: DBConnect, 
    todo_id: int
) -> Optional[aiosqlite.Row]:
    """
    Возвращает aiosqlite.Row или None, если запись не найдена.
    """
    cursor = await connection.execute(
        "SELECT * FROM todos WHERE id = ?", 
        (todo_id,)
    )
    return await cursor.fetchone()

# Обновить Todo
async def update_todo(
    connection: DBConnect, 
    todo_id: int, 
    title: str, 
    description: str, 
    completed: int
) -> int:
    """
    Возвращает количество обновлённых строк (0 если Todo не найден).
    """
    cursor = await connection.execute(
        "UPDATE todos SET title = ?, description = ?, completed = ? WHERE id = ?",
        (title, description, completed, todo_id)
    )
    await connection.commit()
    return cursor.rowcount

# Удалить Todo
async def delete_todo(
    connection: DBConnect, 
    todo_id: int
) -> int:
    """
    Возвращает количество удалённых строк (0 если Todo не найден).
    """
    cursor = await connection.execute(
        "DELETE FROM todos WHERE id = ?", 
        (todo_id,)
    )
    await connection.commit()
    return cursor.rowcount