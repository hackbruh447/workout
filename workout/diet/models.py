from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class userInfo(models.Model):
    name = models.TextField(max_length=20)
    goal = models.IntegerField()
    type = models.BooleanField(default=True)
