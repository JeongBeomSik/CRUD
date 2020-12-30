from django.db import models
from django.conf import settings

# Create your models here.

class User(models.Model):
    userid = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.userid


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40, blank =True)
    introduction = models.TextField(blank=True)

    def __str__(self):
        return self.nickname
