from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ChecklistItem(models.Model):
    # I am using ForeignKey here to create the relationship between my 2 models
    # I want each check list item to belong to a task. 
    # By using on_delete, this should also delete the items if a task gets deleted by the user
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='items'
    )
    text = models.CharField(max_length=200)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text