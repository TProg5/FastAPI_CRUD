import aiosqlite
from aiosqlite import Row

from middle.config import database_settings

async def get_async_connection():
    async with aiosqlite.connect(database_settings.DATABASE_URL) as connection:
        connection.row_factory = Row
        yield connection


async def init_db():
    async with aiosqlite.connect(database_settings.DATABASE_URL) as connection:
        await connection.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL UNIQUE,
                description TEXT NOT NULL, 
                completed INTEGER DEFAULT 0
            )
        """)

        await connection.commit()
