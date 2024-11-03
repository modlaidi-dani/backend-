import pytest

from erp.user.tests.factories import UserFactory


@pytest.fixture
def create_user():
    """Fixture to create a user using the factory."""

    def _create_user(email="testuser@example.com", password="password123"):
        return UserFactory(email=email, password=password)

    return _create_user
