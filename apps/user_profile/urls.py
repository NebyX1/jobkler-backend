from django.urls import path
from .views import (
    UserProfileListView,
    UserProfileDetailView,
    CreateProfileView,
    UserProfileUpdateDeleteView
)

urlpatterns = [
    path('profiles/', UserProfileListView.as_view(), name='profile-list'),  # Listar todos los perfiles
    path('profiles/<int:user_id>/', UserProfileDetailView.as_view(), name='profile-detail'),  # Obtener perfil por ID
    path('profiles/create/', CreateProfileView.as_view(), name='profile-create'),  # Crear un perfil
    path('profiles/<int:user_id>/edit/', UserProfileUpdateDeleteView.as_view(), name='profile-update-delete'),  # Actualizar y eliminar
]
