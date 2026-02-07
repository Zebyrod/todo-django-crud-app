# main_app/views.py

from django.shortcuts import render

# Import models 
from .models import Task
from .models import ChecklistItem


# Create your views here.


def home(request):
    # Render the Home Page
    return render(request, 'home.html')

def about(request):
    # When navigating to /about return the about.html template
    return render(request, 'about.html')


def task_index(request):
    # Render the tasks/index.html with the task list data
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'tasks/detail.html', { 'task': task })



