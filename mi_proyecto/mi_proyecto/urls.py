from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_app.urls')),  # Incluye las rutas de la aplicación 
    path('', lambda request: redirect('login')),  # Redirige la raíz al login
]