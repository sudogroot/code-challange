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


@pytest.fixture
def books_data():
    data = type("InitialData", (object,), {})()
    data.book1 = BookFactory()
    data.book2 = BookFactory()
    data.book3 = BookFactory()
    data.book4 = BookFactory()
    data.book4 = BookFactory()

    return data


def test_get_all_books(client, books_data):
    data = books_data
    response = client.get(reverse("all-books"))

    assert response.status_code == 200
    assert response.data['count'] == 5


def test_add_book(client, user_data):
    url = reverse('all-books')
    data = {
        "title": "wajih",
        "isbn": "1234"
    }

    client.cookies['user_name'] = user_data.user_name
    response = client.post(url, json.dumps(data), content_type='application/json')

    assert response.status_code == 201


def test_add_book_user_name_dose_not_exist(client):
    url = reverse('all-books')
    data = {
        "title": "wajih",
        "isbn": "1234"
    }

    client.cookies['user_name'] = 'i dont exist'
    response = client.post(url, json.dumps(data), content_type='application/json')

    print response.data

    assert response.status_code == 403
    assert response.data['detail'] == 'Adding Book not allowed.'


def test_add_book_existing_isbn(client, user_data):
    url = reverse('all-books')
    client.cookies['user_name'] = user_data.user_name

    data = {
        "title": "book",
        "isbn": "1234"
    }

    client.post(url, json.dumps(data), content_type='application/json')

    data = {
        "title": "book 3",
        "isbn": "1234"
    }
    response = client.post(url, json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    assert 'book with this isbn already exists.' == response.data['detail']


def test_user_books(client, one_book):
    url = reverse('user-books')

    client.cookies['user_name'] = one_book.user_id
    response = client.get(url)

    print response
    # todo assert other data
    assert response.status_code == 200
    assert response.data['count'] == 1
    assert response.data['results'][0]['user'] == one_book.user_id
