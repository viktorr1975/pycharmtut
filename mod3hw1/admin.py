from django.contrib import admin
from mod3hw1.models import Tasks


# Register your models here.
@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    """Отображение модели Cart в админке."""

    list_display = (  # отображение данных по столбцам
        "id",
        "name",
        "done",
        "created",
        "complited",
    )
    search_fields = ("name",)  # поиск задачи по названию
