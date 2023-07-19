# Generated by Django 4.2.1 on 2023-07-17 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('idCargos', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion_Cargo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_periodo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('definicion_proyecto', models.CharField(max_length=255)),
                ('area_destinada', models.CharField(max_length=255)),
                ('finalidad', models.CharField(max_length=255)),
                ('presupuesto_estimado', models.FloatField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_culminacion', models.DateField()),
                ('estado_proyecto', models.CharField(max_length=255)),
                ('porcentaje_completado', models.FloatField()),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_cc.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuarios', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_usuario', models.CharField(max_length=255)),
                ('Contraseña', models.CharField(max_length=255)),
                ('Cargos_idCargos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_cc.cargo')),
                ('Persona_idPersona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_cc.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('idTarea', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion_Tarea', models.CharField(max_length=255)),
                ('Fecha_Limite', models.DateField()),
                ('Estado_Tarea', models.CharField(max_length=255)),
                ('Proyectos_idProyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_cc.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_presupuesto', models.FloatField()),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_cc.periodo')),
            ],
        ),
        migrations.CreateModel(
            name='GastoProyecto',
            fields=[
                ('idGastos_Proyectos', models.AutoField(primary_key=True, serialize=False)),
                ('Presupuesto_Empleado', models.FloatField()),
                ('Presupuesto_idPresupuesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_cc.presupuesto')),
                ('Proyectos_idProyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_cc.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='EncargadoPorProyecto',
            fields=[
                ('idEncargados_por_proyecto', models.AutoField(primary_key=True, serialize=False)),
                ('Persona_idPersona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_cc.persona')),
                ('Proyectos_idProyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_cc.proyecto')),
            ],
        ),
    ]
