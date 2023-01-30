from datetime import date
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from todos.models import Todo


@receiver(pre_save, sender=Todo)
def update_at_handler(sender, instance: Todo, **kwargs):
    instance.updated_at = date.today()
    instance.save()


@receiver(post_save, sender=Todo)
def created_at_handler(sender, instance: Todo, created: bool, **kwargs):
    if created:
        instance.created_at = date.today()
        instance.save()
