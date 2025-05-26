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


class Source(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=200)
    url = models.URLField(blank=True, null=True)
    language_code = models.CharField(max_length=3, blank=True, null=True)
    country_code = models.CharField(max_length=3, blank=True, null=True)


class News(models.Model):
    news_url = models.URLField(unique=True)
    country_code = models.CharField(max_length=3)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=5000)
    publication_date = models.DateTimeField(null=True, blank=True)
    thumbnail_url = models.URLField(
        blank=True, max_length=1000, null=True, default=None
    )
