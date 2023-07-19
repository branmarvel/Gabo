from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import *
from .forms import *


@login_required
def gestion_usuarios(request):
    # Lógica para gestionar usuarios (crear, editar, eliminar)
    return render(request, 'gestion_usuarios.html')


@login_required
def auditorias(request):
    # Lógica para mostrar las auditorías
    return render(request, 'auditorias.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Cambia 'dashboard' por la URL de tu página principal después de iniciar sesión
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registration/register.html', {'form': form})



@login_required
def proyectos_list(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos/proyectos_list.html', {'proyectos': proyectos})


@login_required
def proyecto_detail(request, proyecto_id):
    proyecto = Proyecto.objects.get(pk=proyecto_id)
    return render(request, 'proyectos/proyecto_detail.html', {'proyecto': proyecto})


@login_required
def presupuesto_list(request):
    presupuestos = Presupuesto.objects.all()
    return render(request, 'presupuestos/presupuesto_list.html', {'presupuestos': presupuestos})


@login_required
def estadisticas(request):
    proyectos = Proyecto.objects.all()
    total_proyectos = proyectos.count()
    total_completados = proyectos.filter(estado_proyecto='Completado').count()

    presupuestos = Presupuesto.objects.all()
    total_presupuestos = presupuestos.count()
    total_gastado = presupuestos.aggregate(Sum('cantidad_presupuesto'))['cantidad_presupuesto__sum']

    return render(request, 'estadisticas.html', {
        'total_proyectos': total_proyectos,
        'total_completados': total_completados,
        'total_presupuestos': total_presupuestos,
        'total_gastado': total_gastado,
    })


@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save()
            return redirect('proyecto_detail', proyecto_id=proyecto.id)
    else:
        form = ProyectoForm()
    return render(request, 'crear_proyecto.html', {'form': form})


@login_required
def editar_proyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('proyecto_detail', proyecto_id=proyecto.id)
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'editar_proyecto.html', {'form': form, 'proyecto': proyecto})


@login_required
def eliminar_proyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)
    proyecto.delete()
    return redirect('proyectos_list')


@login_required
def asignar_encargado(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)
    if request.method == 'POST':
        encargado_id = request.POST['encargado_id']
        encargado = Persona.objects.get(id=encargado_id)
        proyecto.encargado = encargado
        proyecto.save()
        return redirect('proyecto_detail', proyecto_id=proyecto.id)
    personas = Persona.objects.all()
    return render(request, 'asignar_encargado.html', {'personas': personas, 'proyecto': proyecto})


@login_required
def crear_presupuesto(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)
    if request.method == 'POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            presupuesto = form.save(commit=False)
            presupuesto.proyecto = proyecto
            presupuesto.save()
            return redirect('presupuesto_list')
    else:
        form = PresupuestoForm()
    return render(request, 'crear_presupuesto.html', {'form': form, 'proyecto': proyecto})


@login_required
def editar_presupuesto(request, presupuesto_id):
    presupuesto = Presupuesto.objects.get(id=presupuesto_id)
    proyecto = presupuesto.proyecto
    if request.method == 'POST':
        form = PresupuestoForm(request.POST, instance=presupuesto)
        if form.is_valid():
            form.save()
            return redirect('presupuesto_list')
    else:
        form = PresupuestoForm(instance=presupuesto)
    return render(request, 'editar_presupuesto.html', {'form': form, 'proyecto': proyecto})


@login_required
def eliminar_presupuesto(request, presupuesto_id):
    presupuesto = Presupuesto.objects.get(id=presupuesto_id)
    proyecto = presupuesto.proyecto
    presupuesto.delete()
    return redirect('presupuesto_list')


@login_required
def detalles_gastos(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)
    presupuestos = Presupuesto.objects.filter(proyecto=proyecto)
    return render(request, 'detalles_gastos.html', {'proyecto': proyecto, 'presupuestos': presupuestos})
