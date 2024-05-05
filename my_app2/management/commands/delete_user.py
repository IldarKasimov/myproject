from django.core.management.base import BaseCommand
from my_app2.models import User


class Command(BaseCommand):
    help = "Delete user by id."

    def add_arguments(self, parser):
        # parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('name', type=str, help='User ID')

    def handle(self, *args, **kwargs):
        # pk = kwargs.get('pk')
        # user = User.objects.filter(pk=pk).first()
        name = kwargs.get('name')
        user = User.objects.filter(name=name).first()
        if user is not None:
            user.delete()
        self.stdout.write(f'{user}')
