from django.contrib import admin

# Register your models here.
from .models import Series, Films, Note, Image

admin.site.register(Series)
admin.site.register(Films)
admin.site.register(Note)
admin.site.register(Image)
