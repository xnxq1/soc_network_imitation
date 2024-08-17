import pytest
from app.auth.dao import DaoAuth

@pytest.mark.parametrize('email, exists, user_id',[
    ('test@test.com', True, 1),
    ('ivan@test.com', True, 2),
    ('wrong@xx.com', False, -1)
])
async def test_get_user_by_email(email, exists, user_id):
        user = await DaoAuth.get_user_by_email(email=email)
        if exists:
            assert user is not None
            assert user.email == email
            assert user.id == user_id
        else:
            assert user is None

@pytest.mark.parametrize('first_name, last_name,age, email, hashed_password, id_db ',[
    ('test', 'testov', 33, 'test@testov.rumbler', 'hashed_password', 3),

])
async def test_add_user_to_db(first_name, last_name,age, email, hashed_password, id_db):
    user_id = await DaoAuth.add_user_to_db(first_name=first_name, last_name=last_name,
                                     age=age, email=email, hashed_password=hashed_password)
    assert user_id == id_db