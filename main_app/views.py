# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Create your views here.

# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    # When navigating to /about return the about.html template
    return render(request, 'about.html')


class Task:
    def __init__(self, name, description, is_complete):
        self.name = name
        self.description = description  # this should be a list
        self.is_complete = is_complete

tasks = [
    Task('Morning Routine', ['Brush teeth', 'Wash face', 'Get dressed'], False),
    Task('Night Routine', ['Brush teeth', 'Shower', 'Set alarm'], False),
    Task('Workout', ['Stretch', 'Run 2 miles', 'Cool down'], True),
]


def task_index(request):
    # Render the tasks/index.html with the task list data
    return render(request, 'tasks/index.html', {'tasks': tasks})

