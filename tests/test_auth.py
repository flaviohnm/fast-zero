from http import HTTPStatus
from fast_zero.security import settings


def test_get_token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert 'access_token' in token
    assert 'token_type' in token


def test_get_token_with_not_found_user(client, user):
    response = client.post(
        '/auth/token',
        data={'username': 'Alice', 'password': user.clean_password},
    )
    # token = response.json()

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_get_token_with_wrong_password(client, user):
    response = client.post(
        '/auth/token', data={'username': user.email, 'password': settings.PASSWORD}
    )
    # token = response.json()

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Incorrect email or password'}
