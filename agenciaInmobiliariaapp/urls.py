from django.urls import path
from . import views  # Aquí sí funciona porque views.py está en esta misma carpeta

urlpatterns = [
    path('', views.listar_arriendos, name='listar_arriendos'),
    path('listar/', views.listar_arriendos, name='listar_arriendos'),
    path('crear/', views.crear_arriendo, name='crear_arriendo'),
    path('editar/<int:id>/', views.editar_arriendo, name='editar_arriendo'),
]