from django.urls import path
from .views import LocationListView, ProfessionListView

urlpatterns = [
    path('locations/', LocationListView.as_view(), name='location-list'),
    path('professions/', ProfessionListView.as_view(), name='profession-list'),
]
