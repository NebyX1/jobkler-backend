from django.urls import path
from .views import FavouriteListView, CreateFavouriteView, FavouriteDeleteView, IsFavouriteView

urlpatterns = [
    path('favourites/', FavouriteListView.as_view(), name='favourite-list'),
    path('favourites/create/', CreateFavouriteView.as_view(), name='favourite-create'),
    path('favourites/<int:pk>/delete/', FavouriteDeleteView.as_view(), name='favourite-delete'),
    path('favourites/is_favourite/<int:profile_id>/', IsFavouriteView.as_view(), name='favourite-is-favourite'),
]
