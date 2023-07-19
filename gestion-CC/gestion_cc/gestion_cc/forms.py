from django import forms
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'  # Incluye todos los campos del modelo Proyecto en el formulario

class PresupuestoForm(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = '__all__'  # Incluye todos los campos del modelo Presupuesto en el formulario


class RegistroForm(UserCreationForm):
    nombres = forms.CharField(max_length=255)
    apellidos = forms.CharField(max_length=255)
    telefono = forms.CharField(max_length=255)
    direccion = forms.CharField(max_length=255)
    cargo = forms.ModelChoiceField(queryset=Cargo.objects.all())

    class Meta:
        model = Usuario
        fields = ['Nombre_usuario', 'Contraseña', 'password2', 'nombres', 'apellidos', 'telefono', 'direccion', 'cargo']

    def clean_Contraseña(self):
        contraseña = self.cleaned_data['Contraseña']
        if not contraseña:
            raise ValidationError("La contraseña es obligatoria.")
        return contraseña

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data['Contraseña'])
        if commit:
            usuario.save()
        return usuario


def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registration/register.html', {'form': form})
