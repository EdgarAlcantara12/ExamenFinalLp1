from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.urls import path


urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Cambiado a 'login/'
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('index/', views.index, name='home'), 
    path('politicas-privacidad/', views.politicas_privacidad, name='politicas_privacidad'), 
    path('herramientas-detalle/', views.herramientas_detalle, name='herramientas_detalle'),
    path('noticias/', views.noticias, name='noticias'),
    path('contacto/', views.contacto, name='contacto'),
]
