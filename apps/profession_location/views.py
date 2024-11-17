from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Location, Profession
from .serializers import LocationSerializer, ProfessionSerializer
from .permissions import IsAdminUserOrReadOnly


# Vista para listar y filtrar departamentos (solo el admin puede crear)
class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['code']  # Permite filtrar por el campo 'code'


# Vista para listar y filtrar profesiones (solo el admin puede crear)
class ProfessionListView(generics.ListAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['code']  # Permite filtrar por el campo 'code'
