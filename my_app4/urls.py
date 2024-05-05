from django.urls import path
from . import views

urlpatterns = [
    path('user/add/', views.user_form, name='user_form'),
    path('forms/', views.many_fields_form, name='many_fields_form'),
    path('user/', views.add_user, name='add_user'),
    path('upload/', views.upload_image, name='upload_image'),
    path('upload2/', views.create_user_file, name='create_user_file'),
    path('get/', views.get_user, name='get_user'),
]
