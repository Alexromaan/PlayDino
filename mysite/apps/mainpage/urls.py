from django.urls import path
from . import views

app_name = 'mainpage'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('perfil/', views.perfil, name='perfil'),
    path('añadir/', views.add, name='añadir'),
    #rutas de las series
    path('delete_serie/<int:pk>', views.delete_serie, name='eliminar serie'),
    path('edit_serie/<int:pk>', views.edit_serie, name='editar serie'),
    #rutas de las peliculas
    path('delete_film/<int:pk>', views.delete_film, name='eliminar pelicula'),
    path('edit_film/<int:pk>', views.edit_film, name='editar pelicula'),
]