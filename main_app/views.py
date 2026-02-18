# main_app/views.py

from django.shortcuts import render, redirect

# Import the built in auth and login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Import models 
from .models import Task
from .models import SubTask

# Import forms
from .forms import TaskForm
from .forms import SubTaskForm

# Importing the timezone from utils
from django.utils import timezone

# Create your views here.


def home(request):
    # Render the Home Page
    return render(request, 'home.html')

def about(request):
    # When navigating to /about return the about.html template
    return render(request, 'about.html')

#  TASK FUNCTION BASED VIEWS 
@login_required
def task_index(request):
    # Render the tasks/index.html with the task list data
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

@login_required
def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    subtasks = SubTask.objects.filter(task=task)
    # subtask_form = SubTask(Form)
    return render(request, 'tasks/detail.html', { 
        'task': task, 
        'subtasks': subtasks,
        # 'subtask_form': subtask_form
    })

@login_required
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

@login_required
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

@login_required
def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task-index')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

# Subtask Function Based Views

@login_required
def subtask_list(request, task_id):
    task = Task.objects.get(id=task_id)
    subtasks = SubTask.objects.filter(task=task)
    return render(request, 'subtasks/subtask_list.html', {
        'task': task,
        'subtasks': subtasks
    })

@login_required    
def subtask_create(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        form = SubTaskForm(request.POST)
        if form.is_valid():
            subtask = form.save(commit=False)
            subtask.task = task

            # this if statement should update the completed_at when the subtask is marked as completed
            if subtask.is_complete:
                subtask.completed_at = timezone.now()

            subtask.save()
            return redirect('subtask-list', task_id=task.id)
    else: 
        form = SubTaskForm()
    return render(request, 'subtasks/subtask_form.html', {
        'form': form,
        'task': task
    })


@login_required
def subtask_delete(request, task_id, subtask_id):
    task = Task.objects.get(id=task_id)
    subtask = SubTask.objects.get(id=subtask_id, task=task)

    if request.method == 'POST':
        subtask.delete()
        return redirect('subtask-list', task_id=task.id)

    return render(request, 'subtasks/subtask_confirm_delete.html', {
        'subtask': subtask,
        'task': task
    })
    
# SIGN UP View

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # If the form is valid then save the user into the database and log them in
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else: 
        form = UserCreationForm()
    return render(request, 'registration/signup.html', { 'form': form }) 
