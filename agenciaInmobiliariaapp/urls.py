from django.urls import path
from . import views  # Aquí sí funciona porque views.py está en esta misma carpeta

urlpatterns = [
    path('', views.listar_arriendo, name='lista_arriendos'),
    path('listar/', views.listar_arriendo, name='listar_arriendo'),
    path('crear/', views.crear_arriendo, name='crear_arriendo'),
    path('editar/<int:id>/', views.editar_arriendo, name='editar_arriendo'),
]