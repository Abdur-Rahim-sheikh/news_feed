import pycountry
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

default_language = str


class User(AbstractUser):
    countries = models.JSONField(default=["nz", "us"])
    sources = models.JSONField(default=["bbc-news", "cnn"])
    keywords = models.JSONField(default=["car", "automobile"])
