from django.urls import path
from . import views
app_name = 'login'

urlpatterns = [
    path('', views.mainlogin, name='mainlogin'),
    path('desconectar/', views.logout_home, name='disconnect'),
    path('registro', views.RegistroUsuario, name='registro'),
    path('/ <key>', views.mainlogin, name='mainlogin')]

