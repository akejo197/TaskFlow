from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tareas, name='listar_tareas'),
    path('agregar/', views.agregar_tarea, name='agregar_tarea'),
    path('eliminar/<int:id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('marcar/<int:id>/', views.marcar_tarea, name='marcar_tarea'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
]