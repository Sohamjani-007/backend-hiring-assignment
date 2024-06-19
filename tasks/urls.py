from django.urls import path
from .views import ProjectListCreateAPIView, ProjectDetailAPIView, TaskListCreateAPIView, TaskDetailAPIView

urlpatterns = [
    path('projects/', ProjectListCreateAPIView.as_view(), name='project_list_create'),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project_detail'),
    path('tasks/', TaskListCreateAPIView.as_view(), name='task_list_create'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task_detail'),
]
