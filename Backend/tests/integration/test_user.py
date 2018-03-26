import pytest
from ..factories import BookFactory, UserFactory
from django.core.urlresolvers import reverse
import json

# def setup_module(module):
#     pass
#
#
# def teardown_module(module):
#     pass

pytestmark = pytest.mark.django_db


@pytest.fixture
def user_data():
    return UserFactory()


def test_creare_user(client):
    url = reverse('user')
    data = {
        'user_name': 'a new user'
    }
    response = client.post(url, json.dumps(data), content_type='application/json')

    assert response.status_code == 200

    assert response.data['user_name'] == 'a new user'


def test_get_user(client):
    url = reverse('user')
    data = {
        'user_name': 'a new user'
    }
    response = client.post(url, json.dumps(data), content_type='application/json')

    assert response.status_code == 200

    assert response.data['user_name'] == 'a new user'
