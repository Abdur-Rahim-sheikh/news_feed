from django.urls import path

from .views import NewsView

urlpatterns = [path("v1/news", NewsView.as_view(), name="user_content")]
