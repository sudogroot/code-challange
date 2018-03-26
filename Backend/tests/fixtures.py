import pytest
from .factories import UserFactory


@pytest.fixture
def user_data():
    return UserFactory()


@pytest.fixture
def client():
    from django.test.client import Client

    return Client()
