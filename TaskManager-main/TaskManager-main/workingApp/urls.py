
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    # path('dashboard', dashboard, name='dashboard'), #show all lists
    path('dashboard', dashboard.as_view(), name='dashboard'), #show all lists
    path('updateTask/<int:pk>', taskUpdate.as_view(), name= 'update_list'),     #show tasks in a list
    path('task/<int:taskId>', taskDescription, name= 'list_descr'),     #show tasks in a list
    path('createTask/', taskCreate.as_view(), name= 'create_list_form'),     #form for adding task
    path('deleteTask/<int:pk>', taskDelete.as_view(), name= 'delete_list'), 


]

