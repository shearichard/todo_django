from __future__ import unicode_literals
from django.db import models


class TodoItem(models.Model):
    label = models.CharField(max_length=512)
    text = models.TextField(null=True)
    done = models.BooleanField(default=False)

    class JSONAPIMeta:
        resource_name = "todos"
