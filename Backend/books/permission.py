from rest_framework import permissions
from .models import Profile
from rest_framework import exceptions


class UserCookiesPermission(permissions.BasePermission):
    message = 'Not authenticated.'

    def has_permission(self, request, view):
        if not request.COOKIES.get('user_name', False):
            raise exceptions.PermissionDenied(detail=self.message)
        return True


class UserExsistPermission(permissions.BasePermission):
    message = 'User dose not exist.'

    def has_permission(self, request, view):
        if not Profile.objects.filter(user_name=request.COOKIES['user_name']).exists():
            raise exceptions.PermissionDenied(detail=self.message)
        return True


class UserPostPermission(permissions.BasePermission):
    message = 'Adding Book not allowed.'

    def has_permission(self, request, view):
        if request.method == 'POST' and (not Profile.objects.filter(user_name=request.COOKIES['user_name']).exists()):
            raise exceptions.PermissionDenied(detail=self.message)

        return True
