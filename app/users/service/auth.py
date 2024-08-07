from app.users.dao import DaoUser
from app.users.errors import ThereIsAUserError, ValidationError
from app.users.hasher import Hasher


class Auth_user:

    @staticmethod
    async def register_user_service(user_data: dict):
        print(user_data)
        user_in_db = await DaoUser.get_user_by_email(user_data['email'])
        print(user_in_db, type(user_in_db))
        if user_in_db is not None:
            raise ThereIsAUserError()

        user_data['password'] = Hasher.get_password_hash(user_data['password'])
        try:
            await DaoUser.add_user_to_db(first_name=user_data['first_name'], last_name=user_data['last_name'],
                                     age=user_data['age'], email=user_data['email'], hashed_password=user_data['password'])
        except:
            raise ValidationError()