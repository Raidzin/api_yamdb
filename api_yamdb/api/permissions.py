from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """Доступ только администратору"""

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_admin)


class ReadOnlyOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_admin
        )


class CreateOrModeratorDeleteOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.method == 'PATCH'
            or request.method == 'DELETE'
            or request.user.is_authenticated
            and (
                request.method == 'POST'
                or request.user.is_admin
            )
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.method == 'PATCH'
            and obj.author == request.user
            or request.user.is_authenticated
            and (
                request.method == 'POST'
                or request.method == 'DELETE'
                and request.user.is_moderator
                or request.user.is_admin
            )
        )
