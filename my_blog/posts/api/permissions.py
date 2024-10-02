from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.mehtod == "GET":
            return True
        else:
            return request.user.is_staff
