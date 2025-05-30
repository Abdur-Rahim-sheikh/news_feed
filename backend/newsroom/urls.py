from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import NewsView, UserView, AuthView, SourceView

urlpatterns = [
    path("v1/news", NewsView.as_view(), name="user_content"),
    path("v1/user", csrf_exempt(UserView.as_view()), name="user"),
    path("v1/login", csrf_exempt(AuthView.as_view()), name="auth"),
    path("v1/sources", SourceView.as_view(), name="sources"),
]
