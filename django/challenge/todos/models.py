from django.db import models


class Todo(models.Model):
    class Priority(models.IntegerChoices):
        LOW = 1
        MEDIUM = 2
        HIGH = 3

    date = models.DateField()
    order = models.IntegerField()
    description = models.TextField()  # todo: wrong field, use CharField with max_len=200
    is_completed = models.BooleanField(default=True)  # todo: wrong default -> False  # Todo, use me in Admin with Select
    priority = models.IntegerField(default=Priority.LOW, choices=Priority.choices)

    def __str__(self):
        return self.description
