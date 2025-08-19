from contextlib import asynccontextmanager
from fastapi import FastAPI
from hard.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield