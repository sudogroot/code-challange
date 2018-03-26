# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import (Book, Comment, Profile, Stars)
from .serializers import BookSerializer, CommentsListSerializer, BookDetailsSerializer, CommentsSerializer, \
    StarsSerializer, StarsListSerializer
from .permission import UserCookiesPermission, UserExsistPermission, UserPostPermission


from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.db.models import Avg


class BookList(generics.ListCreateAPIView):
    """
    View to list all Book
    * Dose not requires any permission

    Post new book
    * Requires user_name cookies and user_name exists

    """
    queryset = Book.objects.all().order_by('-creation_date')
    serializer_class = BookSerializer
    permission_classes = (UserPostPermission,)

    def create(self, request, *args, **kwargs):
        try:
            user_name = request.COOKIES['user_name']
            book = Book.objects.create(user_id=user_name, **request.data)
            return Response(status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            if 'UNIQUE constraint failed: books_book.isbn' == e.message:
                return Response({'detail': 'book with this isbn already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class User(generics.CreateAPIView):
    """
        get or create user identified
         * Dose not requires any permission
    """

    def post(self, request, *args, **kwargs):
        # todo validate requests for views
        user = Profile.objects.get_or_create(**request.data)
        response = Response({'user_name': user[0].user_name}, status=status.HTTP_200_OK)
        return response


class BookDetails(APIView):
    """
    Book details response
    * Dose not requires any permission
    """

    def get_object(self, isbn):
        book = Book.objects.filter(isbn=isbn).annotate(avg_rating=Avg('stars__stars'))
        if not book.exists():
            raise Http404
        return book

    def get(self, request, isbn, format=None):
        book = self.get_object(isbn)
        serializer = BookDetailsSerializer(book[0])
        return Response(serializer.data)


class CommentsPost(generics.CreateAPIView):
    """
    Post new comments on a specific book
    * Requires user_name cookies and user_name exists
    """
    serializer_class = CommentsSerializer
    permission_classes = (UserCookiesPermission, UserExsistPermission,)

    def create(self, request, *args, **kwargs):
        try:
            isbn = kwargs['isbn']
            user_name = request.COOKIES['user_name']
            c = Comment.objects.create(book_id=isbn, user_id=user_name, **request.data)
            return Response(status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist  as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class StarsPost(generics.CreateAPIView):
    """
     Post or update stars on a specific book
     * Requires user_name cookies and user_name exists
     """
    serializer_class = StarsSerializer
    permission_classes = (UserCookiesPermission, UserExsistPermission,)

    def create(self, request, *args, **kwargs):
        try:
            isbn = kwargs['isbn']
            user_name = request.COOKIES['user_name']
            stars = Stars.objects.filter(book_id=isbn, user_id=user_name)
            if stars.exists():
                s = stars[0]
                s.stars = request.data['stars']
                s.full_clean()
                s.save()
                return Response({'detail': 'Rating updated.'}, status=status.HTTP_200_OK)
            Stars.objects.create(book_id=isbn, user_id=user_name, **request.data)
            return Response({'detail': 'Rating created.'}, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist  as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserBooks(generics.ListCreateAPIView):
    """
    View to list all users books
   * Requires user_name cookies and user_name exists
    """

    serializer_class = BookSerializer
    permission_classes = (UserCookiesPermission, UserExsistPermission)

    def get_queryset(self):
        return Book.objects.filter(user_id=self.request.COOKIES['user_name']).order_by('-creation_date')


class UserComments(generics.ListCreateAPIView):
    """
    View to list all users comments.
    * Requires user_name cookies and user_name exists
    """
    serializer_class = CommentsListSerializer
    permission_classes = (UserCookiesPermission, UserExsistPermission)

    def get_queryset(self):
        return Comment.objects.filter(user_id=self.request.COOKIES['user_name']).order_by('-creation_date')


class UserStars(generics.ListCreateAPIView):
    """
    View to list all users stars.
    * Requires user_name cookies and user_name exists
    """
    serializer_class = StarsListSerializer
    permission_classes = (UserCookiesPermission, UserExsistPermission)

    def get_queryset(self):
        return Stars.objects.filter(user_id=self.request.COOKIES['user_name']).order_by('-creation_date')


class CommentsReviews(generics.ListCreateAPIView):
    """
    View to list all reviews comments for user's books.
   * Requires user_name cookies and user_name exists
    """

    serializer_class = CommentsListSerializer
    permission_classes = (UserCookiesPermission, UserExsistPermission)

    def get_queryset(self):
        return Comment.objects.filter(book__user=self.request.COOKIES['user_name']).exclude(
            user_id=self.request.COOKIES['user_name']).order_by('-creation_date')


class StarsReviews(generics.ListCreateAPIView):
    """
    View to list all reviews stars for user's books.
   * Requires user_name cookies and user_name exists
    """

    serializer_class = StarsListSerializer
    permission_classes = (UserCookiesPermission, UserExsistPermission)

    def get_queryset(self):
        return Stars.objects.filter(book__user=self.request.COOKIES['user_name']).exclude(
            user_id=self.request.COOKIES['user_name']).order_by('-creation_date')
