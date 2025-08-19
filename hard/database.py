from typing import AsyncGenerator

import aiosqlite
from aiosqlite import Row, Connection

from hard.core.config import database_settings

async def get_async_connection() -> AsyncGenerator[Connection, None]:
    async with aiosqlite.connect(database_settings.DATABASE_URL) as connection:
        await connection.execute("PRAGMA foreign_keys = ON;")
        connection.row_factory = Row
        yield connection



async def init_db() -> None:
    async for connection in get_async_connection():

        await connection.execute("""               
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )   
        """)
        
        await connection.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                title TEXT NOT NULL UNIQUE,
                description TEXT NOT NULL, 
                completed INTEGER DEFAULT 0,
                user_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        """)

        await connection.commit()