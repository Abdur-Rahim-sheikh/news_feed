from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
def default_countries():
    return ["nz", "us"]


def default_sources():
    return ["bbc-news", "cnn"]


def default_keywords():
    return ["car", "automobile"]


class User(AbstractUser):
    countries = models.JSONField(default=default_countries)
    sources = models.JSONField(default=default_sources)
    keywords = models.JSONField(default=default_keywords)
