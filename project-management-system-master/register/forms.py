from django import forms
from register.models import Company as Comp
from register.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico', required=True)
    company = forms.ModelChoiceField(queryset=Comp.objects.all())

    class Meta:
        model = User
        fields = {
            'username',
            'first_name',
            'last_name',
            'email',
            'company',
            'password1',
            'password2',
        }

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'company': 'Empresa',
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        company = self.cleaned_data['company']

        if commit:
            user.save()
            user_profile = UserProfile.objects.create(user=user, company=Comp.objects.get(name=company))
            user_profile.save()

        return user

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Apellido'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Correo electrónico'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar contraseña'
        self.fields['company'].widget.attrs['class'] = 'form-control'


class CompanyRegistrationForm(forms.Form):
    social_name = forms.CharField(max_length=80, label='Nombre Social')
    name = forms.CharField(max_length=80, label='Nombre')
    email = forms.EmailField(label='Correo electrónico')
    city = forms.CharField(max_length=50, label='Ciudad')
    found_date = forms.DateField(label='Fecha de fundación')

    class Meta:
        model = Comp


    def save(self, commit=True):
        company = Comp()
        company.social_name = self.cleaned_data['social_name']
        company.name = self.cleaned_data['name']
        company.email = self.cleaned_data['email']
        company.city = self.cleaned_data['city']
        company.found_date = self.cleaned_data['found_date']

        if commit:
            company.save()


    def __init__(self, *args, **kwargs):
        super(CompanyRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['social_name'].widget.attrs['class'] = 'form-control'
        self.fields['social_name'].widget.attrs['placeholder'] = 'Nombre Social'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Correo electrónico'
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['placeholder'] = 'Ciudad'
        self.fields['found_date'].widget.attrs['class'] = 'form-control'
        self.fields['found_date'].widget.attrs['placeholder'] = 'Fecha de fundación'


class ProfilePictureForm(forms.Form):
    img = forms.ImageField(label='Imagen')
    class Meta:
        model = UserProfile
        fields = ['img']

    def save(self, request, commit=True):
        user = request.user.userprofile_set.first()
        user.img = self.cleaned_data['img']

        if commit:
            user.save()

        return user

    def __init__(self, *args, **kwargs):
        super(ProfilePictureForm, self).__init__(*args, **kwargs)
        self.fields['img'].widget.attrs['class'] = 'custom-file-input'
        self.fields['img'].widget.attrs['id'] = 'validatedCustomFile'
