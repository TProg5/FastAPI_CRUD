import uvicorn
from typing import Annotated

from fastapi import FastAPI

from middle.lifespan import lifespan
from middle import api

app = FastAPI(lifespan=lifespan)
app.include_router(router=api.router)


if __name__ == "__main__": 
    uvicorn.run(app=app)