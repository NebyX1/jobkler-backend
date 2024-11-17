from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager, models.Manager):
    def _create_user(
        self,
        username,
        email,
        password,
        is_staff,
        is_superuser,
        is_active,
        **extra_fields
    ):
        # Validar el correo electrónico
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError("Debe ingresar un correo electrónico válido.")

        if not username:
            raise ValueError("El nombre de usuario es obligatorio.")

        # Normalizamos el email
        email = self.normalize_email(email)

        # Creamos el usuario
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )

        # Establecemos la contraseña encriptada
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        # Definir campos específicos para el superusuario
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("El superusuario debe tener is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("El superusuario debe tener is_superuser=True.")
        if not password:
            raise ValueError("La contraseña es obligatoria para el superusuario.")

        return self._create_user(username, email, password, **extra_fields)

    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El correo electrónico es obligatorio.")
        if not password:
            raise ValueError("La contraseña es obligatoria.")

        # Crear un usuario normal
        return self._create_user(
            username,
            email,
            password,
            is_staff=False,
            is_superuser=False,
            is_active=False,
            **extra_fields
        )
