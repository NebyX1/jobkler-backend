from django.urls import path
from .views import delete_image, check_image_exists

urlpatterns = [
    path('cloudinary/delete-image/', delete_image, name='delete_image'),
    path('cloudinary/check-image/', check_image_exists, name='check_image_exists'),
]
