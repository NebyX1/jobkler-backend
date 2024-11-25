from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'surname', 'profession', 'state', 'city', 'created_at')
    search_fields = ('user__email', 'name', 'surname', 'profession__name', 'state__name', 'city__name')
    list_filter = ('state', 'city', 'created_at')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Información Personal', {
            'fields': ('user', 'name', 'surname', 'profession', 'state', 'city', 'phone')
        }),
        ('Detalles del Perfil', {
            'fields': ('about', 'description')
        }),
        ('Imágenes', {
            'fields': ('header', 'certificate', 'portfolio1', 'portfolio2', 'portfolio3')
        }),
        ('Tiempos', {
            'fields': ('created_at', 'updated_at')
        }),
    )


admin.site.register(UserProfile, UserProfileAdmin)
