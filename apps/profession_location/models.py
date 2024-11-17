from django.db import models


# Modelo para los departamentos de Uruguay
class Location(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nombre del Departamento")
    code = models.CharField(
        max_length=3,
        unique=True,
        verbose_name="Código del Departamento",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return self.name


# Modelo para las profesiones y oficios
class Profession(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nombre de la Profesión")
    code = models.CharField(
        max_length=3,
        unique=True,
        verbose_name="Código de la Profesión",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Profesión"
        verbose_name_plural = "Profesiones"

    def __str__(self):
        return self.name
