from django.urls import path

from .views import NewsView

urlpatterns = [path("/", NewsView.as_view(), name="user_content")]
