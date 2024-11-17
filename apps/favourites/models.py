from django.db import models
from django.conf import settings
from apps.user_profile.models import UserProfile


class Favourite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favourites",
        verbose_name="Usuario que guarda como favorito",
        help_text="Usuario autenticado que guarda el favorito",
    )
    profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="favourited_by",
        verbose_name="Perfil favorito",
        help_text="Perfil que ha sido marcado como favorito",
    )
    profile_user_id = models.IntegerField(
        verbose_name="ID del Usuario del Perfil Favorito",
        help_text="ID del usuario al que pertenece el perfil marcado como favorito",
        null=True,  # Permitir valores nulos temporalmente
        blank=True,  # Para formularios y validaciones
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación",
        help_text="Fecha en la que se añadió el perfil a favoritos",
    )

    class Meta:
        verbose_name = "Favorito"
        verbose_name_plural = "Favoritos"
        unique_together = ("user", "profile")  # Evita duplicados
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        # Guarda automáticamente el `user.id` del perfil favorito
        if not self.profile_user_id:
            self.profile_user_id = self.profile.user.id
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.user.username} marcó como favorito a {self.profile.user.username}"
        )
