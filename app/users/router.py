from fastapi import APIRouter, HTTPException
from app.users.schemas import SchemasUserForRegister
from app.users.dao import DaoUser
from app.users.hasher import Hasher
from app.users.service.auth import Auth_user
from app.users.errors import ThereIsAUserError, ValidationError

router = APIRouter(prefix="/users", tags=["users"])

@router.post("")
async def register_user(user_data: SchemasUserForRegister):
    user_data = dict(user_data)
    try:
        await Auth_user.register_user_service(user_data)
    except ThereIsAUserError:
        ThereIsAUserError.fast_api_exception()
    except ValidationError:
        ValidationError.fast_api_exception()




@router.get("/all")
async def get_all_users():
    return await DaoUser.get_all_users()
