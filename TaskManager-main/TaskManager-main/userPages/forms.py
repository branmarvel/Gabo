from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class signupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class siginForm():
    pass
# temprrly using the basic html form for login 
# /will upgrade to django forms soon
