from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import *

class dashboard(LoginRequiredMixin, ListView):
    model = TaskList
    context_object_name = 'tasks' # this is used as providing the context in template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(userKey=self.request.user)
        # context['tasks'] = context['tasks'].filter(completionStatus=False).count()

        searchInput = self.request.GET.get('search-area') or ''
        if searchInput:
            # context['tasks'] = context['tasks'].filter(
            #         desc__contains=searchInput )
            context['tasks'] = context['tasks'].filter(
                    name__startswith=searchInput)
        context['searchInput'] = searchInput
        return context


class taskCreate(LoginRequiredMixin, CreateView):
    model = TaskList
    fields = ['name', 'desc', 'completionStatus','deadline']
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.userKey = self.request.user
        return super(taskCreate, self).form_valid(form)


@login_required(login_url='signin')
def taskDescription(request, taskId):
    tasks = TaskList.objects.filter(id=taskId)
    return render(request, 'workingApp/tasks.html', {'tasks':tasks,'taskId':tasks[0].id,'taskName':tasks[0].name, 'deadline': tasks[0].deadline, 'stat': tasks[0].completionStatus})


class taskUpdate(LoginRequiredMixin, UpdateView):
    model = TaskList
    fields = ['name', 'desc', 'completionStatus','deadline']
    success_url = reverse_lazy('dashboard')


class taskDelete(LoginRequiredMixin, DeleteView):
    model = TaskList
    context_object_name = 'tasks'
    success_url = reverse_lazy('dashboard')


