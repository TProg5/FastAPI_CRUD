import uvicorn
from typing import Annotated

from fastapi import FastAPI

from hard.lifespan import lifespan
from hard.users.router import user
from hard.todos.router import todo

app = FastAPI(lifespan=lifespan)
app.include_router(router=user)
app.include_router(router=todo)


if __name__ == "__main__": 
    uvicorn.run(app=app)