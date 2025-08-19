import uvicorn
from typing import Annotated

from fastapi import FastAPI
from fastapi import HTTPException

from easy.schemas import User, APIResponse
from easy.dependencies import DBConnect
from easy.lifespan import lifespan

app = FastAPI(lifespan=lifespan)


@app.post("/register", response_model=APIResponse)
async def register_user(user: User, connection: DBConnect):
    try:
        cursor = await connection.execute(
            """INSERT INTO users (username, password) VALUES (?, ?)""",
            (user.username, user.password)
        )
        await connection.commit()

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return APIResponse(
        message="User success added!", 
        user=User(
            username=user.username, 
            password=user.password
        )
    )
    

if __name__ == "__main__": 
    uvicorn.run(app=app)