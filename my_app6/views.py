from django.shortcuts import render
from django.db.models import Sum
from my_app5.models import Product


def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'Общее количество посчитано в базе данны',
        'total': total,
    }
    return render(request, 'my_app6/total_count.html', context)


def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': 'Общее количество посчитано в представление',
        'total': total,
    }
    return render(request, 'my_app6/total_count.html', context)


def total_in_template(request):
    context = {
        'title': 'Общее количество посчитано в шаблоне',
        'products': Product
    }
    return render(request, 'my_app6/total_count.html', context)
