import pytest

from ..factories import UserFactory, StarsFactory
from django.core.urlresolvers import reverse

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


@pytest.fixture
def user_stars():
    user = UserFactory()
    stars = []
    stars.append(StarsFactory(user=user))
    stars.append(StarsFactory(user=user))
    stars.append(StarsFactory(user=user))
    stars.append(StarsFactory(user=user))
    stars.append(StarsFactory(user=user))
    return stars


def test_user_stars_list(client, user_stars):
    user_stars = user_stars
    url = reverse('user-stars')

    client.cookies['user_name'] = user_stars[0].user
    response = client.get(url)

    assert response.status_code == 200
    assert response.data['count'] == 5


def test_user_stars_no_cookies(client):
    url = reverse('user-stars')

    response = client.get(url)

    assert response.status_code == 403
    assert response.data['detail'] == 'Not authenticated.'


def test_user_stars_user_dose_not_exist(client):
    url = reverse('user-stars')
    client.cookies['user_name'] = 'i dont exists '

    response = client.get(url)

    assert response.status_code == 403
    assert response.data['detail'] == 'User dose not exist.'
