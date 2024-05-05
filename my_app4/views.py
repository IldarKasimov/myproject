import logging
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .forms import UserForm, ManyFieldsForm, ManyFieldsFormWidget, ImageForm, UserImage
from .models import User, UserFile

logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Делаем что-то с данными
            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    return render(request, 'my_app4/user_form.html', {'form': form})


def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            # Делаем что-то с данными
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = ManyFieldsFormWidget()
    return render(request, 'my_app4/many_fields_form.html', {'form': form})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}.')
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'my_app4/user_form.html', {'form': form, 'message': message})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'my_app4/upload_image.html', {'form': form})


def create_user_file(request):
    if request.method == 'POST':
        form = UserImage(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            image = form.cleaned_data['image']
            # fs = FileSystemStorage()
            # fs.save(image.name, image)
            ui = UserFile(name=name, email=email, age=age, image=image)
            ui.save()
            return redirect('get_user')
    else:
        form = UserImage()
    return render(request, 'my_app4/upload_image.html', {'form': form})


def get_user(request):
    users = UserFile.objects.all()
    return render(request, 'my_app4/get.html', {'users': users})