from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile', 'stars', 'created_at')
    search_fields = ('user__email', 'profile__name', 'profile__surname', 'comment')
    list_filter = ('stars', 'created_at')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Información de la Reseña', {
            'fields': ('user', 'profile', 'stars', 'comment')
        }),
        ('Tiempos', {
            'fields': ('created_at', 'updated_at')
        }),
    )


admin.site.register(Review, ReviewAdmin)
