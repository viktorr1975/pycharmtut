from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Tasks
from django.urls import reverse, reverse_lazy
from rest_framework import viewsets, mixins
from .serializers import TasksSerializer
from .filters import TasksFilterSet
from rest_framework.schemas.openapi import AutoSchema

# Create your views here.
class TasksViewSet(
    mixins.ListModelMixin,  # GET /articles
    mixins.CreateModelMixin,  # POST /articles
    mixins.RetrieveModelMixin,  # GET /articles/1
    mixins.DestroyModelMixin,  # DELETE /articles/1
    mixins.UpdateModelMixin,  # PUT /articles/1
    viewsets.GenericViewSet
):
    """DRF API"""

    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
#    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TasksFilterSet
    ordering_fields = ['id', 'name']    #Specifying which fields may be ordered against
    ordering = ['id']                   #default ordering

    schema = AutoSchema(
        tags=['Tasks'],
        component_name='Tasks',
        operation_id_base='Tasks',
    )

class AllTasksListView(ListView):
    """Представление для отображения списка назавершённых задач."""

    model = Tasks
    context_object_name = "tasks"
    template_name = "all_tasks.html"


class MyTasksListView(ListView):
    """Представление для отображения списка назавершённых задач."""

    context_object_name = "tasks"
    queryset = Tasks.objects.filter(complited__isnull=True)
    template_name = "opened_tasks.html"


class TaskDetailView(DetailView):
    """Представление для отображения одной задачи."""

    model = Tasks
    context_object_name = "task"
    template_name = "task_detail.html"


class TaskCreateView(CreateView):
    """Представление для создания одной задачи."""

    model = Tasks
    fields = ["name", "done"]
    template_name = "task_create.html"
    success_url = "/opened_tasks/"


class TaskUpdateView(UpdateView):
    """Представление для редактирования одной задачи."""

    model = Tasks
    context_object_name = "task"
    fields = ("id", "name", "done")
    template_name = "task_update.html"

    def get_success_url(self):
        return reverse("task-update", kwargs=self.kwargs)  # kwargs содержит id задачи


class TaskDeleteView(DeleteView):
    model = Tasks
    context_object_name = "task"
    template_name = "tasks_confirm_delete.html"
    success_url = reverse_lazy(
        "all-tasks"
    )  # пользователь не будет перенаправлен до тех пор, пока представление не завершит удаление записи из базы данных.
    # def get_success_url(self):
    #      return reverse('create')
