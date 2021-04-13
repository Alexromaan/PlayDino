from django.db import models

# Create your models here.
class Permissions:
    EDIT_SERIES = 'Edit series'
    ADD_SERIES = 'Edit client'
    DELETE_SERIES = 'Delete Series'

class Series(models.Model):
    id = models.AutoField(primary_key=True, on_delete ='CASCADE')
    name = models.Charfield(max_length=255)
    platform = models.Charfield(max_lenght=255)
    image = models.ImageField(upload_to='media_pictures')
    season = models.Charfield(max_lenght=255)
    chapter = models.Charfield(max_lenght=255)

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
