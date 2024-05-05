from django.urls import path
from . import views

urlpatterns = [
    path('db/', views.total_in_db, name='total_in_db'),
    path('view/', views.total_in_view, name='total_in_view'),
    path('template/', views.total_in_template, name='total_in_template'),
]
