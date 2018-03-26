# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


class Profile(models.Model):
    user_name = models.CharField(max_length=200, unique=True, primary_key=True)

    def __unicode__(self):
        return self.user_name


class Book(models.Model):
    user = models.ForeignKey(Profile, related_name='books')  # ondelete CASCADE ?
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200, unique=True, primary_key=True)
    creation_date = models.DateTimeField(default=timezone.now())


class Comment(models.Model):
    user = models.ForeignKey(Profile, related_name='comments')  # ondelete CASCADE ?
    book = models.ForeignKey(Book, related_name='comments', )  # ondelete CASCADE ?
    content = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now())

    def save(self, *args, **kwargs):
        try:
            self.book
        except ObjectDoesNotExist as e:
            raise e
        super(Comment, self).save(*args, **kwargs)


class Stars(models.Model):
    user = models.ForeignKey(Profile, related_name='stars')  # ondelete CASCADE ?
    book = models.ForeignKey(Book, related_name='stars')  # ondelete CASCADE ?
    stars = models.IntegerField(default=1,
                                validators=[
                                    MaxValueValidator(5),
                                    MinValueValidator(1)
                                ])
    creation_date = models.DateTimeField(default=timezone.now())

    def save(self, *args, **kwargs):
        try:
            # verify if book exist
            self.book
        except ObjectDoesNotExist as e:
            raise e
        super(Stars, self).save(*args, **kwargs)
