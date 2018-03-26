from rest_framework import serializers
from models import (Book, Comment, Profile, Stars)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user_name',)


class BookSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = ('title', 'isbn', 'user', 'creation_date')


class CommentsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ('content', 'user', 'creation_date')


class StarsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Stars
        fields = ('stars', 'user', 'creation_date')


class BookDetailsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    comments = CommentsSerializer(read_only=True, many=True)
    avg_rating = serializers.FloatField()

    class Meta:
        model = Book
        fields = ('title', 'isbn', 'user', 'comments', 'creation_date','avg_rating')


class CommentsListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    book = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('content', 'user', 'creation_date', 'book')


class StarsListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    book = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Stars
        fields = ('stars', 'user', 'creation_date', 'book')
