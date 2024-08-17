import pytest

from app.users.dao import DaoUser

@pytest.mark.parametrize('user_id, exists',[
    (1, True),
    (2, True),
    (1111, False),
])
async def test_get_user_by_id(user_id, exists):
    user = await DaoUser.get_user_by_id(user_id)
    if exists:
        assert user is not None
        assert user.id == user_id
    else:
        assert user is None


@pytest.mark.parametrize('user_id, exists, exists_posts', [
    (1, True, True),
    (2, True, True),
    (1111, False, False),
])
async def test_get_user_with_posts(user_id, exists, exists_posts):
    user = await DaoUser.get_user_with_posts(user_id)
    if exists:
        print(user.posts)
        assert user is not None
        assert user.id == user_id
        assert user.posts is not None
        if exists_posts:
            assert user.posts[0].post_status is not None
            assert len(user.posts[0].post_status) == 1
    else:
        assert user is None

async def test_get_all_users():
    users = await DaoUser.get_all_users()
    assert users is not None
    for el in users:
        assert isinstance(el, DaoUser.model)


@pytest.mark.parametrize('user_id, first_name, last_name, fullname, age, exists', [
    (1, 'Petya', 'Petrov', 'Petya Petrov', 22, True),
    (2, 'test', 'testov', 'test testov', 33, True),
    (1111, 'test', 'testov', 'test testov', 33, False),
])
async def test_update_user_data(user_id, first_name, last_name, fullname, age, exists):
    user = await DaoUser.update_user_data(user_id, first_name=first_name, last_name=last_name, age=age)
    if exists:
        assert user is not None
        assert user.id == user_id
        assert user.first_name == first_name
        assert user.last_name == last_name
        assert user.fullname == fullname
        assert user.age == age
    else:
        assert user is None