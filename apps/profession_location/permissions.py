from rest_framework import permissions


# Permiso personalizado para permitir solo a administradores crear o modificar
class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Permite GET, HEAD, OPTIONS para todos; POST solo para administradores
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
