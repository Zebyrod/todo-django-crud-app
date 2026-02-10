# main_app/views.py

from django.shortcuts import render, redirect

# Import models 
from .models import Task
from .models import SubTask

# import forms
from .forms import TaskForm

# Create your views here.


def home(request):
    # Render the Home Page
    return render(request, 'home.html')

def about(request):
    # When navigating to /about return the about.html template
    return render(request, 'about.html')

#  TASK FUNCTION BASED VIEWS 
def task_index(request):
    # Render the tasks/index.html with the task list data
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'tasks/detail.html', { 'task': task })

def task_create(request):
    # First I check the form was submitted/POST correctly
    if request.method == 'POST':
        # Next this is binding the user input
        form = TaskForm(request.POST)
        # Running validation on the form 
        if form.is_valid():
        # Save the user input if the form is valid
            form.save()
        # Redirect will help avoid resubmitting on refresh
            return redirect('task-index')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_form.html', {'form': form })

def task_update(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-detail', task_id=task.id)
    else: 
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'task': task})

def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task-index')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

# ChecklistItem Function Based Views
    


