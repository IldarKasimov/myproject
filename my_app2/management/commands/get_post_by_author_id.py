from django.core.management.base import BaseCommand
from my_app2.models import Author, Post


class Command(BaseCommand):
    help = "Get all posts by author id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        posts = Post.objects.filter(author__pk=pk)
        intro = f'All posts of {posts[0].author.name}\n'
        text = list((int(post.get_s()) for post in posts))
        self.stdout.write(f'{intro}{sum(text)}')
