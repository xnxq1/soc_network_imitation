from app.users.dao import DaoUser


async def update_user_data_service(user_data: dict, user_id: int):
    filtered_data = {key: value for key, value in user_data.items() if value is not None}
    user_data = await DaoUser.update_user_data(user_id, **filtered_data)
    return user_data

