from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filters
from rest_framework.exceptions import NotFound
from .models import Favourite
from .serializers import FavouriteSerializer
from apps.user_profile.models import UserProfile


# Filtro para Favourites basado en 'profile__profession__code' y 'profile__location__code'
class FavouriteFilter(filters.FilterSet):
    profession = filters.CharFilter(field_name='profile__profession__code', lookup_expr='iexact')
    location = filters.CharFilter(field_name='profile__location__code', lookup_expr='iexact')

    def filter_queryset(self, queryset):
        if self.data.get('profession', None) in ['', None]:
            self.data = self.data.copy()
            self.data.pop('profession', None)
        if self.data.get('location', None) in ['', None]:
            self.data = self.data.copy()
            self.data.pop('location', None)
        return super().filter_queryset(queryset)

    class Meta:
        model = Favourite
        fields = ['profession', 'location']


# Vista para listar los favoritos del usuario autenticado
class FavouriteListView(generics.ListAPIView):
    serializer_class = FavouriteSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FavouriteFilter

    def get_queryset(self):
        # Filtra los favoritos por el usuario autenticado
        return Favourite.objects.filter(user=self.request.user)


# Vista para crear un favorito
class CreateFavouriteView(generics.CreateAPIView):
    serializer_class = FavouriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        # Pasar el contexto del request al serializer
        return {'request': self.request}


# Vista para eliminar un favorito
class FavouriteDeleteView(generics.DestroyAPIView):
    serializer_class = FavouriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except NotFound:
            return Response({"detail": "El favorito especificado no existe o no es tuyo"}, status=status.HTTP_404_NOT_FOUND)


class IsFavouriteView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, profile_id, *args, **kwargs):
        user = request.user
        try:
            profile = UserProfile.objects.get(id=profile_id)
        except UserProfile.DoesNotExist:
            return Response({"detail": "El perfil especificado no existe"}, status=status.HTTP_404_NOT_FOUND)

        is_favorited = Favourite.objects.filter(user=user, profile=profile).exists()
        return Response({"is_favorited": is_favorited}, status=status.HTTP_200_OK)
