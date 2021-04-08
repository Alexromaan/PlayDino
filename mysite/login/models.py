from django.db import models
from django.contrib.auth.models import User


# aqui voy a crear la base de datos que tendra a los usuarios y administradores

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=36, null=False)

    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(max_length=9)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username