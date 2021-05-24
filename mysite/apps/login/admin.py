from django.contrib import admin

# Register your models here.

class UserMetaAdmin(admin.ModelAdmin):
    search_fields = 'user__username'
