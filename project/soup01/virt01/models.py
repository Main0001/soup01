from django.db import models
from django.db.models import JSONField


class TaskModel(models.Model):
    field = models.CharField(max_length=255)
    data = JSONField()

    def __str__(self):
        return self.data, self.field
