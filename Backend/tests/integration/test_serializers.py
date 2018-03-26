import pytest
from ..factories import BookFactory, UserFactory, CommentsFactory, StarsFactory
from books.serializers import *

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
def books_data():
    return BookFactory.create(comments=3, stars=4)


def test_book_serializer(one_book):
    serialzed_book = BookSerializer(one_book)
    keys = ['title', 'isbn', 'user', 'creation_date']

    assert serialzed_book.data.keys() == keys


@pytest.fixture
def one_book():
    return BookFactory()


def test_profile_serializer(user_data):
    serialzed_profile = ProfileSerializer(user_data)
    keys = ['user_name']

    assert serialzed_profile.data.keys() == keys


def test_comments_serializer():
    comments = CommentsFactory()
    serialzed_comments = CommentsSerializer(comments)
    keys = ['content', 'user', 'creation_date']

    assert serialzed_comments.data.keys() == keys


def test_comments_list_serializer():
    comments = CommentsFactory()
    serialzed_comments = CommentsListSerializer(comments)
    keys = ['content', 'user', 'creation_date', 'book']

    assert serialzed_comments.data.keys() == keys
    assert serialzed_comments.data['book'] == comments.book.isbn


def test_stars_serializer():
    stars = StarsFactory()
    serialzed_stars = StarsSerializer(stars)
    keys = ['stars', 'user', 'creation_date']

    assert serialzed_stars.data.keys() == keys

    # TODO CALCULATE AVRAGE  STARS


def test_stars_list_serializer():
    stars = StarsFactory()
    serialzed_stars = StarsListSerializer(stars)
    keys = ['stars', 'user', 'creation_date', 'book']

    assert serialzed_stars.data.keys() == keys
    assert serialzed_stars.data['book'] == stars.book.isbn

#
# def test_book_details_serializer(books_data):
#     book = books_data
#     serialzed_book = BookDetailsSerializer(book)
#     keys = ['title', 'isbn', 'user', 'comments', 'stars', 'creation_date']
#
#     assert serialzed_book.data.keys() == keys
