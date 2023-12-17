from django.core.management.base import BaseCommand
from django.utils import timezone
import random
from datetime import timedelta
from todos.models import Todo  # Adjust this import based on your model's location

class Command(BaseCommand):
    help = 'Populate the database with Todo instances for the next 60 days, excluding weekends'

    def handle(self, *args, **kwargs):
        start_date = timezone.now()
        for day in range(60):
            current_date = start_date + timedelta(days=day)
            # Skip weekends (Saturday=5, Sunday=6)
            if current_date.weekday() in [5, 6]:
                continue

            # Create an average of 400 Todos per day
            for _ in range(400):
                # Assuming your Todo model has fields like 'name', 'description', etc.
                # Adjust the following line according to your Todo model's fields
                Todo.objects.create(
                    name=f'Todo {current_date.strftime("%Y-%m-%d")} #{_ + 1}',
                    description='Automatically generated Todo',
                    due_date=current_date,
                    # Add other fields as necessary
                )
            self.stdout.write(self.style.SUCCESS(f'Successfully created Todos for {current_date.strftime("%Y-%m-%d")}'))
