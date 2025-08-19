from typing import Annotated

from fastapi import APIRouter
from fastapi import HTTPException, Body
from hard.dependencies import DBConnect

from hard.schemas import TodoWithUserResponse
from hard.users.schemas import User, UserResponse, DeleteUserResponse
from hard.users.repository import register_user, delete_user

user = APIRouter(
    prefix="/api"
)

@user.post(
    "user/register", 
    response_model=UserResponse, 
    status_code=201
)
async def register_user_endpoint(user: User, connection: DBConnect):
    try:
        await register_user(
            connection=connection,
            username=user.username,
            password=user.password
        )
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return UserResponse(
        message="User success added!", 
        user=User(
            username=user.username, 
            password=user.password
        )
    )


@user.delete(
    "/users/{user_id}", 
    response_model=DeleteUserResponse, 
    status_code=201
)
async def delete_user_endpoint(user_id: int, connection: DBConnect):
    try:
        rowcount = await delete_user(
            connection=connection,
            user_id=user_id
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    if rowcount == 0:
        raise HTTPException(status_code=404, detail={"User Not Found"})
    
    return DeleteUserResponse(
        message="User success deleted!", 
        user_id=user_id
    )
