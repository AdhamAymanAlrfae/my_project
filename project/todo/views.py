from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.urls import reverse_lazy


class Log_in(LoginView):
    fields = "__all__"
    template_name = "todo/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home")

class Home(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)

        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(titel__icontains=search_input)
        context['search_input'] = search_input
        return context

class Show_Task(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task.html'
    

class Create_Task(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['titel', 'discription','complete']
    success_url = reverse_lazy('home')
    template_name = 'todo/create.html'
    def form_valid(self, form):
        form.instance.user = self.request.user

        return super(Create_Task,self).form_valid(form)

class Update_Task(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['titel', 'discription','complete']
    success_url = reverse_lazy('home')
    template_name = 'todo/create.html'

class Delete_Task(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('home')
    template_name = "todo/delete.html"
    context_object_name = "task"

class Register_Page(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)


        return super(Register_Page, self ).form_valid(form)