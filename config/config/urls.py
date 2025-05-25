from django.contrib import admin
from django.urls import path, include

# from libros.views import home_view


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('accounts.urls')),  
    path('', include('libros.urls')),
    path('', include('prestamos.urls')),
    path('', include('reseñas.urls')),
    
]