from django.db import models
from django.conf import settings
from apps.user_profile.models import UserProfile  # Importamos UserProfile desde la app user_profile


class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews_given',
        verbose_name='Usuario',
        help_text='Usuario que escribe la reseña'
    )
    profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='reviews_received',
        verbose_name='Perfil',
        help_text='Perfil del usuario al que se dirige la reseña'
    )
    stars = models.PositiveSmallIntegerField(
        verbose_name='Estrellas',
        help_text='Calificación entre 1 y 5',
        choices=[(i, str(i)) for i in range(1, 6)]
    )
    comment = models.TextField(
        verbose_name='Comentario',
        help_text='Contenido de la reseña'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de actualización'
    )

    class Meta:
        verbose_name = 'Reseña'
        verbose_name_plural = 'Reseñas'
        ordering = ['-created_at']
        unique_together = ('user', 'profile')  # Para evitar reseñas duplicadas

    def __str__(self):
        return f"Reseña de {self.user.username} a {self.profile.name}"
