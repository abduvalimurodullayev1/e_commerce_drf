from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow any authenticated user
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow safe methods (GET, HEAD, OPTIONS) or if the user owns the object
        return request.method in SAFE_METHODS or obj.user == request.user
