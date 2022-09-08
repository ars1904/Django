from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class IsAuthor(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_author
        return False