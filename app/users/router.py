from fastapi import APIRouter, HTTPException
from app.users.schemas import SchemasUserForRegister
from app.users.dao import DaoUser
from app.users.auth.hasher import Hasher
router = APIRouter(prefix="/users", tags=["users"])

@router.post("")
async def register_user(user_data: SchemasUserForRegister):
    user_in_db = await DaoUser.get_user_by_email(user_data.email)

    if user_in_db:
        raise HTTPException(status_code=409, detail='Такой пользователь уже есть')

    user_data.password = Hasher.get_password_hash(user_data.password)
    await DaoUser.add_user_to_db(first_name=user_data.first_name, last_name=user_data.last_name,
                                 age=user_data.age, email=user_data.email, hashed_password=user_data.password)




@router.get("/all")
async def get_all_users():
    return await DaoUser.get_all_users()
