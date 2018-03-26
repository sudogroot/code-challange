import pytest

from tests.factories import CommentsFactory
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


@pytest.fixture
def user_comments():
    user = UserFactory()
    comments = []
    comments.append(CommentsFactory(user=user))
    comments.append(CommentsFactory(user=user))
    comments.append(CommentsFactory(user=user))
    comments.append(CommentsFactory(user=user))
    comments.append(CommentsFactory(user=user))
    return comments


def test_user_comments_list(client, user_comments):
    user_comments = user_comments
    url = reverse('user-comments')

    client.cookies['user_name'] = user_comments[0].user
    response = client.get(url)

    assert response.status_code == 200
    assert response.data['count'] == 5


def test_user_comments_no_cookies(client):
    url = reverse('user-comments')

    response = client.get(url)

    assert response.status_code == 403
    assert response.data['detail'] == 'Not authenticated.'


def test_user_comments_user_dose_not_exist(client):
    url = reverse('user-comments')
    client.cookies['user_name'] = 'i dont exists '

    response = client.get(url)

    assert response.status_code == 403
    assert response.data['detail'] == 'User dose not exist.'
