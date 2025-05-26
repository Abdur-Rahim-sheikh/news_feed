from django.contrib import admin

from .models import News, Source, User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "email",
        "countries",
        "sources",
        "keywords",
        "is_active",
        "is_superuser",
    ]

    fields = [
        "username",
        "email",
        "countries",
        "sources",
        "keywords",
        "is_active",
        "is_superuser",
    ]


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = [
        "news_url",
        "source",
        "country_code",
        "title",
        "source_id",
        "summary",
        "publication_date",
        "thumbnail_url",
    ]


@admin.register(Source)
class Source(admin.ModelAdmin):
    list_display = ["id", "name", "url", "country_code", "language_code"]
