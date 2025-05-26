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
        articles = [
            {
                "news_url": "https://apnews.com/article/south-carolina-shooting-little-river-7525cdaf1ffa5ac7b7e15c96fe74ecc0",
                "title": "At least 11 hurt in South Carolina beach town shooting - AP News",
                "summary": "Authorities say at least 11 people were taken to hospitals after a shooting in a South Carolina beach town. Horry County Police did not give the conditions of anyone hurt or detail how they were injured in the incident, which happened about 9:30 p.m. Sunday i…",
                "published_at": "2025-05-26T11:51:00Z",
                "thumbnail_url": "https://dims.apnews.com/dims4/default/574d94d/2147483647/strip/true/crop/2593x1459+0+135/resize/1440x810!/quality/90/?url=https%3A%2F%2Fassets.apnews.com%2F5d%2Fec%2Fe2b517e513ffb6daf590461ad927%2Fcceeca456fd549a0a1f893b8eb346f53",
            }
        ]
        return JsonResponse({"articles": articles}, status=200)
