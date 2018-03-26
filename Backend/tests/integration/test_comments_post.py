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


@pytest.fixture
def one_book():
    return BookFactory()


def test_post_comment(client, user_data, one_book):
    url = reverse('book-comment', kwargs={'isbn': one_book.isbn})
    data = {'content': 'this is the new comment'}

    client.cookies['user_name'] = user_data.user_name
    response = client.post(url, json.dumps(data), content_type='application/json')

    assert response.status_code == 201


def test_post_comment_books_dose_not_exist(client, user_data):
    url = reverse('book-comment', kwargs={'isbn': 'i dont exist'})
    data = {'content': 'this is the new comment'}

    client.cookies['user_name'] = user_data.user_name
    response = client.post(url, json.dumps(data), content_type='application/json')

    assert response.status_code == 400


def test_post_comment_no_cookies(client, one_book):
    url = reverse('book-comment', kwargs={'isbn': one_book.isbn})
    data = {'content': 'this is the new comment'}

    response = client.post(url, json.dumps(data), content_type='application/json')

    assert response.status_code == 403
    assert response.data['detail'] == 'Not authenticated.'


def test_post_comment_user_dose_not_exist(client, one_book):
    url = reverse('book-comment', kwargs={'isbn': one_book.isbn})
    data = {'content': 'this is the new comment'}
    client.cookies['user_name'] = 'i dont exists '

    response = client.post(url, json.dumps(data), content_type='application/json')

    assert response.status_code == 403
    assert response.data['detail'] == 'User dose not exist.'
