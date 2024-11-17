from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.users.urls')),
    path('api/', include('apps.user_profile.urls')),
    path('api/', include('apps.profession_location.urls')),
    path('api/', include('apps.reviews.urls')),
    path('api/', include('apps.cloudinary_permissions.urls')),
    path('api/', include('apps.favourites.urls')),

    # Redirigir rutas no definidas en /api a la página principal
    re_path(r'^api/.*$', RedirectView.as_view(url='https://jobkler.com', permanent=False), name='custom_404'),
]
