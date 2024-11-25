from django.db import models
from django.conf import settings
from apps.profession_location.models import Profession, State, City


# Modelo de Perfil de Usuario
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="Usuario",
        help_text="Usuario al que está asociado este perfil"
    )
    name = models.CharField(max_length=100, verbose_name="Nombre")
    surname = models.CharField(max_length=100, verbose_name="Apellido")
    profession = models.ForeignKey(
        Profession,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Profesión",
        help_text="Profesión del usuario"
    )
    state = models.ForeignKey(
        State,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Estado",
        help_text="Estado o departamento del usuario"
    )
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Ciudad",
        help_text="Ciudad del usuario"
    )
    about = models.TextField(verbose_name="Sobre mí", help_text="Una breve descripción sobre el usuario")
    description = models.TextField(verbose_name="Descripción", help_text="Descripción detallada del perfil")
    phone = models.CharField(max_length=15, verbose_name="Teléfono")
    header = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="URL de Imagen de Perfil"
    )
    certificate = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="URL de Certificado"
    )
    portfolio1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="URL de Portafolio 1"
    )
    portfolio2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="URL de Portafolio 2"
    )
    portfolio3 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="URL de Portafolio 3"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuarios"
        ordering = ['-created_at']

    def __str__(self):
        profession_name = self.profession.name if self.profession else "Sin profesión"
        return f"{self.name} {self.surname} - {profession_name}"
