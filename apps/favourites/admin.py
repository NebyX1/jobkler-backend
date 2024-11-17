from django.contrib import admin
from .models import Favourite


class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile', 'profile_user_id', 'created_at')  # Agregado profile_user_id
    search_fields = ('user__email', 'user__username', 'profile__name', 'profile__surname', 'profile_user_id')  # Agregado profile_user_id
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'profile_user_id')  # Agregado profile_user_id como readonly

    fieldsets = (
        ('Información del Usuario', {
            'fields': ('user',)
        }),
        ('Perfil Favorito', {
            'fields': ('profile', 'profile_user_id')  # Agregado profile_user_id
        }),
        ('Tiempos', {
            'fields': ('created_at',)
        }),
    )


admin.site.register(Favourite, FavouriteAdmin)
