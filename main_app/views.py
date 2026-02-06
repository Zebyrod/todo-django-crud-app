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

# I had to add the actual CheckList as another class to be used within the Tasks 
# class ChecklistItem:
#     def __init__(self, text, is_complete=False):
#         self.text = text
#         self.is_complete = is_complete


# class Task:
#     def __init__(self, name, items, is_complete=False):
#         self.name = name
#         # self.description = description  # this should be a list
#         # I first made a quick mock data example so I could make my initial pages and start to get a sense for the layout and design I want
#         # Now I am going back and revising my data before I make my models. I wanted the original data to be a list that can be checked off as completed
#         self.items = items
#         self.is_complete = is_complete

# tasks = [
#     Task(
#         'Morning Routine',
#         [
#             ChecklistItem('Brush teeth', True),
#             ChecklistItem('Wash face', False),
#             ChecklistItem('Get dressed', False),
#         ]
#     ),
#     Task(
#         'Night Routine',
#         [
#             ChecklistItem('Brush teeth', True),
#             ChecklistItem('Shower', False),
#             ChecklistItem('Set alarm', True),
#         ]
#     ),
#     Task(
#         'Workout',
#         [
#             ChecklistItem('Stretch', True),
#             ChecklistItem('Run 2 miles', True),
#             ChecklistItem('Cool down', True),
#         ],
#         is_complete=True
#     ),
# ]


def task_index(request):
    # Render the tasks/index.html with the task list data
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})



