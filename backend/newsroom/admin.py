from django.contrib import admin

from .models import News, Source, User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "email",
        "country_codes",
        "source_ids",
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
        "source_id",
        "country_code",
        "get_users",
        "title",
        "summary",
        "publication_date",
        "thumbnail_url",
    ]

    def get_users(self, obj):
        return ", ".join(user.username for user in obj.users.all())

    get_users.short_description = "users"


@admin.register(Source)
class Source(admin.ModelAdmin):
    list_display = ["id", "name", "url", "country_code", "language_code"]
    search_fields = ["id", "name"]
