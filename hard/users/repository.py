from aiosqlite import Cursor
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