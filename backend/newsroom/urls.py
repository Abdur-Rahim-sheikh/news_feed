from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import NewsView, UserView

urlpatterns = [
    path("v1/news", NewsView.as_view(), name="user_content"),
    path("v1/user", csrf_exempt(UserView.as_view()), name="user"),
]
