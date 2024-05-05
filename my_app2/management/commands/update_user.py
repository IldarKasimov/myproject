from django.core.management.base import BaseCommand
from my_app2.models import User


class Command(BaseCommand):
    help = "Update user name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('name', type=str, help='User name')
        parser.add_argument('email', type=str, help='Email')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        email = kwargs.get('email')
        user = User.objects.filter(pk=pk).first()
        user.email = email
        user.name = name
        user.save()
        self.stdout.write(f'{user}')
