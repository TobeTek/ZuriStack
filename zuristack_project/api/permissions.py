from rest_framework import permissions

class IsCreatorOrAdminReadOnly(permissions.BasePermission):
    edit_methods = ('PUT', 'PATCH')

    def has_object_permission(self, request, view, obj):
        # If it's a safe method (GET, HEAD, OPTIONS) allow
        if request.method in permissions.SAFE_METHODS:
            return True 
        
        if request.user.is_staff and request.method not in self.edit_methods:
            return True 

        if request.user.is_superuser:
            return True 
        
        if request.user == obj:
            return True 

    