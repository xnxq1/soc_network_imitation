import pytest
from httpx import AsyncClient

router_prefix = '/auth'

@pytest.mark.parametrize('first_name, last_name, age, email, password, status_code',[
    ('Maks', 'Maksbetov', 10, 'maks@test.com', '1234', 200),
    ('Maks', 'Maksbetov', 10, 'maks@test.com', '1234', 409),
    ('Maks', 'Maksbetov', -1, 'testtest@test.com', '1234', 422),
    ('Rayan', 'Gosling', 33, 'wrongemail', 'qwrqqw', 422),
    ('Rayan', 'GGGGGosling', 33, 'nice@email.com', 'qwrqqw', 409)
])
async def test_register_user(first_name, last_name, age, email, password, status_code, async_client: AsyncClient):
    url = f'{router_prefix}/register'
    response = await async_client.post(url=url, json={
        'first_name': first_name, 'last_name': last_name, 'age': age, 'email': email, 'password': password})
    assert response.status_code == status_code
    if status_code == 200:
        assert response.cookies.get('access_token') is not None


@pytest.mark.parametrize('email, password, status_code', [
    ('test@test.com', 'test', 200),
    ('ivan@test.com', 'test', 200),
    ('ivan@test.com', 'wrong', 401),
    ('fredericofelleni@test.com', 'wrong', 401),
    ('wrong', 'wrong', 422),
])
async def test_login_user(email, password, status_code, async_client: AsyncClient):
    url = f'{router_prefix}/login'
    response = await async_client.post(url=url, json={
        'email': email, 'password': password
    })

    assert response.status_code == status_code
    if status_code == 200:
        assert response.cookies.get('access_token') is not None


async def test_logout_user(authenticate_client: AsyncClient):
    url = f'{router_prefix}/logout'
    response = await authenticate_client.post(url=url)

    assert response.status_code == 200
    assert response.cookies.get('access_token') is None

    response = await authenticate_client.post(url=url)
    assert response.status_code == 401
