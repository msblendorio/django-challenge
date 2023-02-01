import random
from datetime import date, datetime

from django.test import TestCase

from todos.models import Todo


class TodoTestCase(TestCase):
    def create(self):
        obj = Todo(
            date=date.today(),
            order=random.randint(0, 999),
            description='Anim non officia elit aliqua aute aliqua minim',
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        obj.save()
