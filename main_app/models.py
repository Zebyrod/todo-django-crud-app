from django.db import models

# Create your models here.
class Task(models.Model):
# Making major additions to the models now that base functionality is working for both
# Plan is to add these into the models then work through all the CRUD again to ensure all features are present
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]

    name = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    priority = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default='M'
    )

    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

class SubTask(models.Model):
    # I am using ForeignKey here to create the relationship between my 2 models
    # I want each check list item to belong to a task. 
    # By using on_delete, this should also delete the items if a task gets deleted by the user
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='subtasks'
    )
    description = models.CharField(max_length=200)

#  Adding in ordering of the SubTasks is a big want for me
# I am implementing priority for the overall tasks but there can still be priority within the subtasks as well
    order = models.PositiveIntegerField(default=0)

    is_complete = models.BooleanField(default=False)
    # I wanted to add the completed_at as a way to track data within the app. Hopefully as I scale the application this can be used
    # Current plan is for maybe employees to have access with a login and the company can track who is completing what
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['order']