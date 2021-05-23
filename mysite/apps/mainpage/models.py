from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.forms import ModelForm


class Permissions:
    EDIT_SERIES = 'Edit series'
    ADD_SERIES = 'Edit client'
    DELETE_SERIES = 'Delete Series'


class Series(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    season = models.IntegerField()
    chapter = models.IntegerField()
    image = models.ImageField(upload_to='static/media', default='default.png')

    def __str__(self):
        return self.name


class Films(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/media', default='default.png')

    def __str__(self):
        return self.name

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=500)
    serie = models.ForeignKey(Series, to_field='id', on_delete=models.CASCADE, null=True)
    film = models.ForeignKey(Films, to_field='id', on_delete=models.CASCADE, null=True)

    def __srt__(self):
        return self.text
