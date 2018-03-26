import pytest
from ..factories import BookFactory, UserFactory, StarsFactory
from django.core.urlresolvers import reverse
import random

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


def test_get_book_details(client, one_book):
    url = reverse('book-details', kwargs={'isbn': one_book.isbn})
    response = client.get(url)

    assert response.data['isbn'] == one_book.isbn


def test_get_book_details_not_found(client):
    url = reverse('book-details', kwargs={'isbn': 'i dont exist'})
    response = client.get(url)

    assert response.status_code == 404


@pytest.fixture
def book_stars():
    data = type("InitialData", (object,), {})()
    data.book = BookFactory()
    stars = [random.randint(1, 5) for i in range(10)]
    for i in stars:
        StarsFactory(stars=i, book=data.book)
    data.avg = sum(stars) / float(len(stars))
    return data


def test_get_book_avg_stars_details(client, book_stars):
    data = book_stars
    url = reverse('book-details', kwargs={'isbn': data.book.isbn})
    response = client.get(url)

    assert response.data['isbn'] == data.book.isbn
    assert response.data['avg_rating'] == data.avg

    # test keys here instead of serailizer test for simplicity
    keys = ['title', 'isbn', 'user', 'comments', 'creation_date', 'avg_rating']
    assert response.data.keys() == keys
