# tasks/urls.py

from django.urls import path
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<str:_id>/', TaskDetailView.as_view(), name='task-detail'),
]
