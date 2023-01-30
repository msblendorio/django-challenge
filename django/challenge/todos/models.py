from django.db import models


class Todo(models.Model):
    class Priority(models.IntegerChoices):
        LOW = 1
        MEDIUM = 2
        HIGH = 3

    date = models.DateField()
    order = models.IntegerField()
    description = models.CharField(max_length=128)
    is_completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=Priority.LOW, choices=Priority.choices)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.description
