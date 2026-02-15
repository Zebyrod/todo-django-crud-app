from django import forms
from .models import Task
from .models import SubTask

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'priority',
            'due_date',
            'is_complete'
            ]
        
        # The widget here I found online it is supposed to offer a cleaner look for the date time field. Otherwise Django renders a plain one
        widgets = {
            'due_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local'
            })
        }

class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = [
            'description', 
            'order',
            'is_complete',
            ]

        # I want the completed_at to be automatically tracked and updated when the user is checking off the tasks as completed which is why it is not in this model
