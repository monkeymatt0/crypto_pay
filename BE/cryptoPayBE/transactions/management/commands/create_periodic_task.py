from django.core.management.base import BaseCommand
from django_celery_beat.models import IntervalSchedule, PeriodicTask
import json


class Command(BaseCommand):
    message = "Created a priodic task to check pending transactions"

    def handle(self, *args, **kwargs):
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=10, period=IntervalSchedule.SECONDS
        )

        task, created = PeriodicTask.objects.get_or_create(
            interval=schedule,
            task="transactions.tasks.monitor_transactions_status",
            args=json.dumps([]),
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f"Created periodic task: {task.name}"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Task already exists: {task.name}"))
