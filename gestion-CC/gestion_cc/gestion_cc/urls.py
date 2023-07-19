from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.estadisticas, name='dashboard'),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('proyectos/', views.proyectos_list, name='proyectos_list'),
    path('proyecto/<int:proyecto_id>/', views.proyecto_detail, name='proyecto_detail'),
    path('presupuestos/', views.presupuesto_list, name='presupuesto_list'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
    path('crear_proyecto/', views.crear_proyecto, name='crear_proyecto'),
    path('editar_proyecto/<int:proyecto_id>/', views.editar_proyecto, name='editar_proyecto'),
    path('eliminar_proyecto/<int:proyecto_id>/', views.eliminar_proyecto, name='eliminar_proyecto'),
    path('asignar_encargado/<int:proyecto_id>/', views.asignar_encargado, name='asignar_encargado'),
    path('crear_presupuesto/<int:proyecto_id>/', views.crear_presupuesto, name='crear_presupuesto'),
    path('editar_presupuesto/<int:presupuesto_id>/', views.editar_presupuesto, name='editar_presupuesto'),
    path('eliminar_presupuesto/<int:presupuesto_id>/', views.eliminar_presupuesto, name='eliminar_presupuesto'),
    path('detalles_gastos/<int:proyecto_id>/', views.detalles_gastos, name='detalles_gastos'),
    path('gestion_usuarios/', views.gestion_usuarios, name='gestion_usuarios'),
    path('auditorias/', views.auditorias, name='auditorias'),
]
