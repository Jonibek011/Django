from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomModel(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
