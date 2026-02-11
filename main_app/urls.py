# main_app/urls.py

from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    # Routes will be added here
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # TASK URLS
    path('tasks/', views.task_index, name='task-index'),
    path('tasks/create/', views.task_create, name='task-create'),
    path('tasks/<int:task_id>/', views.task_detail, name='task-detail'),
    path('tasks/<int:task_id>/edit', views.task_update, name='task-edit'),
    path('tasks/<int:task_id>/delete/', views.task_delete, name='task-delete'),

    # SUBTASK URLS
    path('tasks/<int:task_id>/subtasks/', views.subtask_list, name='subtask-list'),
]
