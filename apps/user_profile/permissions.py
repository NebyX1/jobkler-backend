from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permite solo al propietario del perfil editar o eliminar.
    """

    def has_object_permission(self, request, view, obj):
        # Permisos de lectura permitidos para cualquier solicitud
        if request.method in permissions.SAFE_METHODS:
            return True
        # Permisos de escritura permitidos solo para el propietario
        return obj.user == request.user
