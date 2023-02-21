"""pycharmtut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from mod3hw1.views import AllTasksListView, MyTasksListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView
from django.urls import path, include
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("", AllTasksListView.as_view(), name="all-tasks"),
    path("opened_tasks/", MyTasksListView.as_view(), name="list"),
    path("create_task/", TaskCreateView.as_view(), name="create"),
    path("task/<int:pk>", TaskDetailView.as_view(), name="task-detail"),
    path("edit_task/<int:pk>", TaskUpdateView.as_view(), name="task-update"),
    path('delete_task/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    path("api/", include("mod3hw1.urls")),

    path('openapi/', get_schema_view(
        title="Studying",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
]
