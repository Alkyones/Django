from .permissions import IsStaffEditorPermissions
from rest_framework import permissions
#
class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermissions]


class UserQuerySetMixin():
    user_field = 'user'
    allow_staff_view = False
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff and self.allow_staff_view:
            return super().get_queryset()
        return super().get_queryset().filter(user=self.request.user)
