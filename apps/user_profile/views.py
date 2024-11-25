from rest_framework import generics, permissions
from django_filters import rest_framework as filters
from rest_framework.exceptions import NotFound
from .models import UserProfile
from .serializers import UserProfileSerializer
from .permissions import IsOwnerOrReadOnly


# Filtro para UserProfile basado en 'profession__code', 'state__code' y 'city__code'
class UserProfileFilter(filters.FilterSet):
    profession = filters.CharFilter(field_name='profession__code', lookup_expr='iexact')
    state = filters.CharFilter(field_name='state__code', lookup_expr='iexact')
    city = filters.CharFilter(field_name='city__code', lookup_expr='iexact')

    def filter_queryset(self, queryset):
        # Limpia filtros vacíos o nulos
        self.data = {k: v for k, v in self.data.items() if v not in ['', None]}
        return super().filter_queryset(queryset)

    class Meta:
        model = UserProfile
        fields = ['profession', 'state', 'city']


# Vista para listar perfiles filtrados
class UserProfileListView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserProfileFilter


# Vista para obtener un perfil por ID de usuario (GET /api/profiles/<int:user_id>/)
class UserProfileDetailView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]  # Público

    def get_object(self):
        user_id = self.kwargs['user_id']
        try:
            return UserProfile.objects.get(user_id=user_id)
        except UserProfile.DoesNotExist:
            raise NotFound({"detail": "Este usuario no tiene un perfil creado"})


# Vista para crear un perfil (POST /api/profiles/create/)
class CreateProfileView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados

    def perform_create(self, serializer):
        # Asocia el perfil con el usuario autenticado
        serializer.save(user=self.request.user)


# Vista para actualizar y eliminar un perfil (PUT/PATCH/DELETE /api/profiles/<int:user_id>/edit/)
class UserProfileUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]  # Solo el propietario puede modificar

    def get_object(self):
        user_id = self.kwargs['user_id']
        try:
            return UserProfile.objects.get(user_id=user_id)
        except UserProfile.DoesNotExist:
            raise NotFound({"detail": "Este usuario no tiene un perfil creado"})
