from django import forms
from .models import Task
from .models import SubTask

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name']

