from django_filters import rest_framework as dj_filters
from .models import Tasks


class TasksFilterSet(dj_filters.FilterSet):
    """Набор фильров для представления для модели задач."""

    #    name = dj_filters.CharFilter(field_name="name", lookup_expr="icontains")

    #    order_by_field = "ordering"  # the query parameter name (http://example.com/api/users?ordering=username)
    #    is_active = dj_filters.BooleanFilter(field_name="done", exclude=True, label="is_active")

    class Meta:
        model = Tasks

        fields = [
            "title",
        ]
