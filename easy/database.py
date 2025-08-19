import aiosqlite
from aiosqlite import Row

from easy.config import database_settings

async def get_async_connection():
    async with aiosqlite.connect(database_settings.DATABASE_URL) as connection:
        connection.row_factory = Row
        yield connection


async def init_db():
    async with aiosqlite.connect(database_settings.DATABASE_URL) as connection:
        await connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        """)
        await connection.commit()
