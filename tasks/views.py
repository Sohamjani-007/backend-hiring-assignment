from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from .custom_response import CustomMetaDataMixin
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer


# todo :  @here Please read README2.md for Curl commands to TEST out each and every below API.

class ProjectListCreateAPIView(CustomMetaDataMixin, APIView):
    """
    # Example of a POST request
    POST /api/projects/
    {
    "name": "New Project",
    "description": "Project description",
    "client": "Client Name",
    "start_date": "2023-10-01",
    "end_date": "2023-12-31"
    }
    # Expected output: The created project data with status 201 Created
    """
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 10
        projects = Project.objects.all()
        result_page = paginator.paginate_queryset(projects, request)
        serializer = ProjectSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetailAPIView(CustomMetaDataMixin, APIView):
    """
    # Example of how to use the ProjectDetailAPIView class in a Django URL configuration
    from django.urls import path
    from .views import ProjectDetailAPIView

    urlpatterns = [
        path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
    ]
    """
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return None

    def get(self, request, pk):
        project = self.get_object(pk)
        if project is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        if project is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = self.get_object(pk)
        if project is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskListCreateAPIView(CustomMetaDataMixin, APIView):
    """
    # Example GET request to retrieve a paginated list of tasks
    GET /api/tasks/

    # Example POST request to create a new task
    POST /api/tasks/
    {
        "name": "New Task",
        "description": "Task description",
        "project": 1,
        "status": "To Do"
    }
    """
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 10
        tasks = Task.objects.all()
        result_page = paginator.paginate_queryset(tasks, request)
        serializer = TaskSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPIView(CustomMetaDataMixin, APIView):
    """
    task_detail_view = TaskDetailAPIView()
    task = task_detail_view.get_object(1)
    if task:
        print("Task found:", task)
    else:
        print("Task not found")
    """
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return None

    def get(self, request, pk):
        task = self.get_object(pk)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
