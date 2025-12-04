from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import TaskForm
from django.views.generic.edit import CreateView, UpdateView
from .models import Task

# Create your views here.
from django.views.generic import ListView
from .models import Task # Припустимо, у вас є модель Post


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'task_list'
    ordering = ['create_ad'] # Сортування за датою публікації (від нових до старих)
    

class TaskDetailView(ListView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
    
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('home')