from typing import Annotated

from fastapi import Depends
from aiosqlite import Connection

from hard.database import get_async_connection

DBConnect = Annotated[Connection, Depends(get_async_connection)]