"""Contains class definition for a read only permission"""

from rest_framework import permissions


class IsReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow only read only
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True

        return False
