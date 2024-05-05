from django.core.management.base import BaseCommand
from my_app2.models import User


class Command(BaseCommand):
    help = "Get all users."

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        self.stdout.write(f'{users}')
        for u in users:
            self.stdout.write(f'{u.name}, {u.age}')
