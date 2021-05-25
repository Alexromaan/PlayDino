from django.contrib import admin

# Register your models here.
from .models import Series, Films, Image

admin.site.register(Series)
admin.site.register(Films)
admin.site.register(Image)
