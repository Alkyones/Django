from .permissions import IsStaffEditorPermissions
from rest_framework import permissions
#
class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermissions]