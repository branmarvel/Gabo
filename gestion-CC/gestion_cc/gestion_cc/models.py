from django.db import models
from django.apps import apps
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission



class Cargo(models.Model):
    idCargos = models.AutoField(primary_key=True)
    Descripcion_Cargo = models.CharField(max_length=255)

    def __str__(self):
        return self.Descripcion_Cargo
    
    class Meta:
        app_label = apps.get_containing_app_config(__name__).name


class Persona(models.Model):
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    
    class Meta:
        app_label = apps.get_containing_app_config(__name__).name



class Usuario(AbstractUser):
    idUsuarios = models.AutoField(primary_key=True)
    Nombre_usuario = models.CharField(max_length=255, unique=True)
    Contraseña = models.CharField(max_length=255)
    Cargos_idCargos = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    Persona_idPersona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    groups = models.ManyToManyField(
        Group,
        related_name='usuarios',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuarios',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.Nombre_usuario
    
    class Meta:
        app_label = apps.get_containing_app_config(__name__).name


class Proyecto(models.Model):
    creador = models.ForeignKey(Persona, on_delete=models.CASCADE)
    definicion_proyecto = models.CharField(max_length=255)
    area_destinada = models.CharField(max_length=255)
    finalidad = models.CharField(max_length=255)
    presupuesto_estimado = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_culminacion = models.DateField()
    estado_proyecto = models.CharField(max_length=255)
    porcentaje_completado = models.FloatField()

    def __str__(self):
        return self.definicion_proyecto
    
    class Meta:
        app_label = apps.get_containing_app_config(__name__).name


class EncargadoPorProyecto(models.Model):
    idEncargados_por_proyecto = models.AutoField(primary_key=True)
    Persona_idPersona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Proyectos_idProyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    class Meta:
        app_label = apps.get_containing_app_config(__name__).name


class Periodo(models.Model):
    descripcion_periodo = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion_periodo
    
    class Meta:
        app_label = apps.get_containing_app_config(__name__).name


class Presupuesto(models.Model):
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    cantidad_presupuesto = models.FloatField()

    def __str__(self):
        return f"Presupuesto {self.periodo}"
    
    class Meta:
        app_label = apps.get_containing_app_config(__name__).name


class GastoProyecto(models.Model):
    idGastos_Proyectos = models.AutoField(primary_key=True)
    Presupuesto_Empleado = models.FloatField()
    Proyectos_idProyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    Presupuesto_idPresupuesto = models.ForeignKey(Presupuesto, on_delete=models.CASCADE)

    class Meta:
        app_label = apps.get_containing_app_config(__name__).name


class Tarea(models.Model):
    idTarea = models.AutoField(primary_key=True)
    Descripcion_Tarea = models.CharField(max_length=255)
    Fecha_Limite = models.DateField()
    Estado_Tarea = models.CharField(max_length=255)
    Proyectos_idProyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    class Meta:
        app_label = apps.get_containing_app_config(__name__).name
