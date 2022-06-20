from rest_framework import permissions

class IsStaffEditorPermissions(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        if user.is_staff or user.is_superuser:
            return True
        return False
    