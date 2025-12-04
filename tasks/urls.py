from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from .views import TaskCreateView, TaskListView, TaskDetailView, TaskUpdateView

urlpatterns = [
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path("", TaskListView.as_view(), name="home"),
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
]
