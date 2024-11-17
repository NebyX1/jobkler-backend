from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import UserManager


class User(AbstractUser, PermissionsMixin):
    # Campos del modelo
    username = models.CharField(
        max_length=100, unique=True, verbose_name="Nombre de usuario"
    )
    email = models.EmailField(
        max_length=254, unique=True, verbose_name="Correo electrónico"
    )

    # Estado del usuario
    is_staff = models.BooleanField(
        default=False, verbose_name="Es personal administrativo"
    )
    is_superuser = models.BooleanField(default=False, verbose_name="Es superusuario")
    is_active = models.BooleanField(default=False, verbose_name="Está activo")

    # Definir que el login será por correo electrónico
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    # Manager personalizado
    objects = UserManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    # Añadir los related_name para evitar conflictos con auth.User
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  # Cambia el related_name para evitar conflictos
        verbose_name="Grupos",
        blank=True,
        help_text="Los grupos a los que pertenece este usuario.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # Cambia el related_name para evitar conflictos
        verbose_name="Permisos del usuario",
        blank=True,
        help_text="Permisos específicos para este usuario.",
    )

    # Método para mostrar el nombre del usuario en el admin
    def __str__(self):
        return self.username
