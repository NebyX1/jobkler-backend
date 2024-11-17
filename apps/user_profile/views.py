from rest_framework import generics, permissions
from .models import UserProfile
from .serializers import UserProfileSerializer
from .permissions import IsOwnerOrReadOnly
from django_filters import rest_framework as filters
from rest_framework.exceptions import NotFound


# Filtro para UserProfile basado en 'profession__code' y 'location__code'
class UserProfileFilter(filters.FilterSet):
    profession = filters.CharFilter(field_name='profession__code', lookup_expr='iexact')
    location = filters.CharFilter(field_name='location__code', lookup_expr='iexact')

    def filter_queryset(self, queryset):
        if self.data.get('profession', None) in ['', None]:
            self.data = self.data.copy()
            self.data.pop('profession', None)
        if self.data.get('location', None) in ['', None]:
            self.data = self.data.copy()
            self.data.pop('location', None)
        return super().filter_queryset(queryset)

    class Meta:
        model = UserProfile
        fields = ['profession', 'location']


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
