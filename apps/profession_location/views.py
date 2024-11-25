from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import State, City, Profession
from .serializers import StateSerializer, CitySerializer, ProfessionSerializer
from .permissions import IsAdminUserOrReadOnly


# Vista para listar y filtrar estados (solo el admin puede crear)
class StateListView(generics.ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['code']  # Permite filtrar por el campo 'code'


# Vista para listar y filtrar ciudades (solo el admin puede crear)
# Vista para listar y filtrar ciudades
class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['state__code']  # Permite filtrar por estado usando el código

    def get_queryset(self):
        # Verifica si el estado está en los parámetros
        state_code = self.request.query_params.get('state')
        if state_code:
            return City.objects.filter(state__code=state_code)
        return super().get_queryset()


# Vista para listar y filtrar profesiones (solo el admin puede crear)
class ProfessionListView(generics.ListAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['code']  # Permite filtrar por el campo 'code'
