from app.users.dao import DaoUser
from app.users.errors import ValidationError


async def update_user_data_service(user_data: dict, user_id: int):
    filtered_data = {key: value for key, value in user_data.items()
                     if key != 'email' and key != 'hashed_password' and value is not None}
    try:
        user_data = await DaoUser.update_user_data(user_id, **filtered_data)
    except:
        raise ValidationError()
    return user_data

