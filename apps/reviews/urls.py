from django.urls import path
from .views import ReviewListView, ReviewCreateView, ReviewDeleteView

urlpatterns = [
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
]
