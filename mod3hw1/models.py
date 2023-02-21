from django.db import models
from django.utils import timezone

# Create your models here.
from django.db import models


class Tasks(models.Model):
    """Задачи"""

    title = models.TextField(
        blank=False, null=False, help_text="название задания"
    )  # null is purely database-related, whereas blank is validation-related
    is_active = models.BooleanField(blank=False, null=False, help_text="сделано")
    created = models.DateTimeField(
        blank=False, null=False, auto_now=True, help_text="дата и время создания"
    )
    complited = models.DateTimeField(
        blank=True, null=True, help_text="дата и время завершения"
    )

    def __str__(self):
        """переопределение строкового представления объекта."""
        return f"Список задач {self.id}|{self.title}|{self.is_active}|{self.created}|{self.complited}"

    class Meta:
        """установка дополнительных параметров модели"""

        verbose_name_plural = "Tasks"

    def save(self, *args, **kwargs) -> None:
        """Переопределение сохранения.
        Устанавливаем время завершения в случае
        наличие отметки выполнения и отсутствии времени завершения
        """
        if self.is_active is False and self.complited is None:
            self.complited = timezone.now()
        elif self.is_active is True:
            self.complited = None
        return super().save(*args, **kwargs)
