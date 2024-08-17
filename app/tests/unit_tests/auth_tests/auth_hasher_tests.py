from app.auth.service.hasher import Hasher
import pytest

@pytest.mark.parametrize('password',[
    ('test'),
    ('test111'),
])
def test_get_password_hash(password):
    hash = Hasher.get_password_hash(password)
    assert hash is not None
    assert len(hash) == 60