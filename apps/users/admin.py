from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    # Campos que se mostrarán en el formulario de edición en el panel de administración
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # Campos que se mostrarán al agregar un nuevo usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active'),
        }),
    )
    list_display = ('username', 'email', 'is_active', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('email',)


# Registrar el modelo personalizado con los cambios
admin.site.register(User, UserAdmin)
