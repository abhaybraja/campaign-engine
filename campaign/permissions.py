from rest_framework.permissions import BasePermission

class AdminOnly(BasePermission):
    message = "Access denied: Only admin allowed!"
    def has_permission(self, request, view):

        return request.user and request.user.is_authenticated and request.user.role == 'admin'

class UserOnly(BasePermission):
    message = "Access denied: Only user allowed!"
    def has_permission(self, request, view):

        return request.user and request.user.is_authenticated and request.user.role == 'user'