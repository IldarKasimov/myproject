# Generated by Django 5.0.4 on 2024-04-26 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app4', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
