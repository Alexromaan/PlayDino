from django.urls import path
from . import views

app_name = 'mainpage'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('añadir/', views.add, name='añadir'),
    path('añadir_nota/', views.add_note, name='añadir nota'),
    # rutas del buscador de la API
    path('buscar/', views.fetch, name='buscar'),
    path('save/<str:pk>', views.save_fetch, name='save'),
    # rutas de las series
    path('delete_serie/<int:pk>', views.delete_serie, name='eliminar serie'),
    path('edit_serie/<int:pk>', views.edit_serie, name='editar serie'),
    # rutas de las peliculas
    path('delete_film/<int:pk>', views.delete_film, name='eliminar pelicula'),
    path('edit_film/<int:pk>', views.edit_film, name='editar pelicula'),
    #rutas del perfil
    path('perfil/', views.perfil, name='perfil'),
    path('cambiar_user/', views.change_username, name='cambiar user'),
]
