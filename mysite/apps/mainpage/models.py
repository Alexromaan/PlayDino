from django.db import models

# Create your models here.
class Permissions:
    EDIT_SERIES = 'Edit series'
    ADD_SERIES = 'Edit client'
    DELETE_SERIES = 'Delete Series'


class Series(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    chapter = models.CharField(max_length=100)

    def __str__(self):
        return self.name