from typing import Optional
from aiosqlite import Cursor, Row
from hard.dependencies import DBConnect


async def register_user(
    connection: DBConnect,
    username: str,
    password: str
) -> int:
    cursor: Cursor = await connection.execute(
        """INSERT INTO users (username, password) VALUES (?, ?)""", 
        (username, password)
    )

    await connection.commit()
    return cursor.lastrowid


async def delete_user(
    connection: DBConnect,
    user_id: int
) -> int:
    cursor: Cursor = await connection.execute(
        """DELETE FROM users WHERE id = ?""", 
        (user_id,)
    )

    await connection.commit()
    return cursor.rowcount

async def get_user_todos(
    connection: DBConnect,
    user_id: int
) -> Optional[Row]:
    cursor: Cursor = await connection.execute("""
        SELECT users.id AS user_id, users.username AS username, todos.id AS todo_id, todos.title, todos.description, todos.completed 
        FROM todos INNER JOIN users ON todos.user_id = users.id WHERE users.id = ?;
    """, (user_id,))

    return await cursor.fetchall()