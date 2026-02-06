from django.contrib import admin
from .models import Task
from .models import ChecklistItem

# Register your models here.
admin.site.register(Task)
admin.site.register(ChecklistItem)