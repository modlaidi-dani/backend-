import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_user_registration(api_client):

    # Payload for registration
    payload = {
        "email": "newuser@example.com",
        "first_name": "New",
        "last_name": "User",
        "password": "password123"
    }

    response = api_client.post(reverse('register'), payload, format='json')

    assert response.status_code == 201
    assert response.data['user']['email'] == payload['email']


@pytest.mark.django_db
def test_user_login_jwt(api_client, create_user):

    # Adjusted indentation to be a multiple of 4 spaces
    create_user(email="testlogin@example.com", password="password123")

    login_payload = {
        "email": "testlogin@example.com",
        "password": "password123"
    }

    response = api_client.post(reverse('token_obtain_pair'), login_payload, format='json')

    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data
