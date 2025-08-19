from contextlib import asynccontextmanager
from fastapi import FastAPI
from easy.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield