from django.http import HttpRequest, JsonResponse
from django.views import View
# import jsonresponse


class NewsView(View):
    def get(self, request: HttpRequest):
        # if not request.user.is_authenticated:
        #     return JsonResponse({"error": "User not authenticated"}, status=401)

        # username = request.user.username
        # email = request.user.email
        # first_name = request.user.first_name
        html = "<h2>hello abir</h2> are your mail"
        return JsonResponse({"message": html}, status=200)
