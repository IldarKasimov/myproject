from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from .models import Author, Post


def hello(request):
    return HttpResponse("Hello World from function!")


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")


def year_post(request, year):
    text = ""
    ...  # формируем статьи за год
    return HttpResponse(f"Posts from {year}<br>{text}")


class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        ...  # формируем статьи за год и месяц
        return HttpResponse(f"Posts from {month}/{year}<br>{text}")


def post_detail(request, year, month, slug):
    ...  # Формируем статьи за год и месяц по идентификатору.
    # Пока обойдёмся без запросов к базе данных
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python, list() или []",
        "content": "В процессе написания очередной программы задумался над тем, "
                   "какой способ создания списков в Python работает быстрее..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def my_view(request):
    context = {'name': 'John'}
    return render(request, 'my_app3/my_templates.html', context)


class TemplIf(TemplateView):
    template_name = "my_app3/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        # context['number'] = 5 # передали в kwargs в пути urls
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'my_app3/templ_for.html', context)


def index(request):
    return render(request, 'my_app3/index.html')


def about(request):
    return render(request, 'my_app3/about.html')


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]  # сортируем в обратном порядке по ИД 5 последних
    return render(request, 'my_app3/author_posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'my_app3/post_full.html', {'post': post})


def get_all(request):
    authors = Author.objects.all()
    return render(request, 'my_app3/all_authors.html', {'authors': authors})


def del_author(request, author_id):
    # author = get_object_or_404(Author, pk=author_id)  # доп способ получить автора по ID
    author = Author.objects.get(pk=author_id)
    author.delete()
    return redirect('get_all')


def post_full2(request, author_id):
    posts = Post.objects.filter(author=author_id)
    return render(request, 'my_app3/post_full2.html', {'posts': posts})
