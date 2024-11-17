from django.contrib import admin
from .models import Location, Profession


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
