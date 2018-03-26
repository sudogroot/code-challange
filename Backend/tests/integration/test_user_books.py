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
def user_books():
    user = UserFactory()
    books = []
    books.append(BookFactory(user=user))
    books.append(BookFactory(user=user))
    books.append(BookFactory(user=user))
    books.append(BookFactory(user=user))
    books.append(BookFactory(user=user))
    return books


def test_user_book_list(client, user_books):
    user_books = user_books
    url = reverse('user-books')

    client.cookies['user_name'] = user_books[0].user
    response = client.get(url)

    assert response.status_code == 200
    assert response.data['count'] == 5


def test_user_books_no_cookies(client):
    url = reverse('user-books')

    response = client.get(url)

    assert response.status_code == 403
    assert response.data['detail'] == 'Not authenticated.'


def test_user_books_user_dose_not_exist(client):
    url = reverse('user-books')
    client.cookies['user_name'] = 'i dont exists '

    response = client.get(url)

    assert response.status_code == 403
    assert response.data['detail'] == 'User dose not exist.'
