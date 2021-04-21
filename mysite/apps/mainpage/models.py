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
    image = models.ImageField(upload_to='media_pictures')
    season = models.CharField(max_length=100)
    chapter = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def create_series(name: str, platform: str, image: image = None, season: str = None, chapter: str = None):
        series = Series(
            name=name,
            platform=platform,
            image=image,
            season=season,
            chapter=chapter,
        )
        return series
