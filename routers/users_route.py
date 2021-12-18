from fastapi import APIRouter
from models.users_model import User

router = APIRouter()

@router.post("/", response_model=User)
async def create_user(user: User):
    return user