from rest_framework import permissions

class IsSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
    
class IsProjectMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        
        if request.method in permissions.SAFE_METHODS:
            if hasattr(obj, 'membros'):
                return obj.membros.filter(usuario=request.user).exists()
            
            if hasattr(obj, 'projeto'):
                return obj.projeto.membros.filter(usuario=request.user).exists()
        
        return False