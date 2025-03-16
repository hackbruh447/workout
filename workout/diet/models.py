from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=20, default = "null")
    goal = models.IntegerField(default = 0)
    type = models.BooleanField(default=True)
    points = models.IntegerField(default = 0)
    challenges_completed = models.IntegerField(default = 0)


    def __str__(self):
        return f"{self.name}"
