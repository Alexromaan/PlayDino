from django.urls import path
from . import views

app_name = 'mainpage'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('series/', views.add_series, name='series'),
    path('perfil/', views.perfil, name='perfil'),
    path('delete/<int:pk>', views.delete, name='eliminado'),
    path('edit/<int:pk>', views.edit, name='editar'),
]