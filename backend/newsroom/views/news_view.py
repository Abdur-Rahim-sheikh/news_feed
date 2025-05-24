from django.http import HttpRequest, HttpResponse
from django.views import View


class NewsView(View):
    def get(self, request: HttpRequest):
        if not request.user.is_authenticated:
            return HttpResponse("Not a signed in User")

        username = request.user.username
        email = request.user.email
        # first_name = request.user.first_name
        html = f"<h2>hello {username}</h2> are your mail {email}"
        return HttpResponse(html)
