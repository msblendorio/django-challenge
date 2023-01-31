from datetime import date

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


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


@receiver(pre_save, sender=Todo)
def update_at_handler(sender, instance: Todo, **kwargs):
    instance.updated_at = date.today()
    instance.save()


@receiver(post_save, sender=Todo)
def created_at_handler(sender, instance: Todo, created: bool, **kwargs):
    if created:
        instance.created_at = date.today()
        instance.save()
