from django.contrib import admin
from .models import State, City, Profession


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    list_filter = ('code',)  # Filtro por código de estado


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'code')  # Mostrar el estado al que pertenece
    search_fields = ('name', 'code', 'state__name')  # Permitir búsqueda por nombre de estado y ciudad
    list_filter = ('state',)  # Filtro por estado
    ordering = ('state__name', 'name')  # Ordenar por nombre de estado y luego por ciudad

    def get_queryset(self, request):
        # Sobrescribimos el queryset para prefetch de estado (optimización)
        queryset = super().get_queryset(request)
        return queryset.select_related('state')


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    list_filter = ('code',)  # Filtro por código de profesión
