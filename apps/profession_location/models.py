from django.db import models


# Modelo para los estados/provincias/departamentos
class State(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nombre del Estado")
    code = models.CharField(
        max_length=5,
        unique=True,
        verbose_name="Código del Estado"
    )

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    def __str__(self):
        return self.name


# Modelo para las ciudades
class City(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre de la Ciudad")
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name="cities",
        verbose_name="Estado"
    )
    code = models.CharField(
        max_length=5,
        unique=True,
        verbose_name="Código de la Ciudad"
    )

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        unique_together = ("name", "state")  # Evitar nombres duplicados en el mismo estado

    def __str__(self):
        return f"{self.name}, {self.state.name}"


# Modelo para las profesiones y oficios
class Profession(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nombre de la Profesión")
    code = models.CharField(
        max_length=5,
        unique=True,
        verbose_name="Código de la Profesión"
    )

    class Meta:
        verbose_name = "Profesión"
        verbose_name_plural = "Profesiones"

    def __str__(self):
        return self.name
