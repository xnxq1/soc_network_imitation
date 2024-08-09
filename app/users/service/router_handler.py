from app.users.dao import DaoUser
from app.users.errors import ThereIsAUserError, ValidationError, WrongDataForAuthError
from app.users.service.hasher import Hasher


class Auth_user:


    @staticmethod
    async def register_user_service(user_data: dict) -> int:
        user_in_db = await DaoUser.get_user_by_email(user_data['email'])
        if user_in_db is not None:
            raise ThereIsAUserError()

        user_data['password'] = Hasher.get_password_hash(user_data['password'])
        try:
            return await DaoUser.add_user_to_db(first_name=user_data['first_name'], last_name=user_data['last_name'],
                                     age=user_data['age'], email=user_data['email'], hashed_password=user_data['password'])
        except:
            raise ValidationError()

    @staticmethod
    async def login_user_service(user_data: dict) -> int:
        user_in_db = await DaoUser.get_user_by_email(user_data['email'])
        if not user_in_db or not Hasher.verify_password(user_data['password'], user_in_db.hashed_password):
            raise WrongDataForAuthError()
        return user_in_db.id



async def update_user_data_service(user_data: dict, user_id: int):
    filtered_data = {key: value for key, value in user_data.items() if value is not None}
    print(filtered_data)
    user_data = await DaoUser.update_user_data(user_id, **filtered_data)
    print(1)
    return user_data
