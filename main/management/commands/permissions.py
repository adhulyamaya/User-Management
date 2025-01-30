from rest_framework import permissions

class IsMainAdmin(permissions.BasePermission):
    """
    Custom permission to allow access only to main admins.
    """
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name="main_admin").exists()

class IsStaff(permissions.BasePermission):
    """
    Custom permission to allow access only to staff.
    """
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name="staff").exists()
