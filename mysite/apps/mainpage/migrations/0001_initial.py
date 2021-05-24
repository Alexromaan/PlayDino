# Generated by Django 3.1.7 on 2021-05-24 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fetch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=200)),
                ('imdb', models.CharField(max_length=20, null=True)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('time', models.CharField(default='00:00:00', max_length=100)),
                ('image', models.ImageField(default='default.png', upload_to='static/media')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('season', models.IntegerField(default=1)),
                ('chapter', models.IntegerField(default=1)),
                ('image', models.ImageField(default='default.png', upload_to='static/media')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(max_length=500)),
                ('film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainpage.films')),
                ('serie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainpage.series')),
            ],
        ),
    ]
