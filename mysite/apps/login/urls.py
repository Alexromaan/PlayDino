from django.urls import path
from . import views
app_name = 'login'

urlpatterns = [
    path('', views.mainlogin, name='mainlogin'),
    path('desconectar', views.logout_home, name='logout'),
    path('registro', views.RegistroUsuario, name='registro'),
]

