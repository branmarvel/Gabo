from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from workingApp.views import index
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView as signinView
from .forms import *

from workingApp.models import *

def index(request): # used for a new comer for login/signup or to reaad about our app
    return render(request, 'userPagesTemplates/index.html')

# not using user creation form or class based view here in order to practice fun based view
def signup(request):
    if request.method == 'POST':
        # form = UserCreationForm(data= request.POST)
        form = signupForm(data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:   
        # form = UserCreationForm()
        form = signupForm()
    return render(request, 'userPagesTemplates/signup.html', {'form':form})
#  in case of is_valid()== false this should return to the same page of signup thats why we are returning outside the else.

class customeSignin(signinView):
    template_name = 'userPagesTemplates/signin.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('dashboard')



# def signin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         # user exists :: ?
#         user = authenticate(request, username=username, password= password )
#         if user is not None:
#         # login
#             login(request, user)
#             return redirect('dashboard')
#         else:
#             # showing message on invalid credentials
#             messages.error(request, "invalid login details")
#     return render(request, 'userPagesTemplates/signin.html')

def signout(request):
    logout(request)
    return redirect('index')
