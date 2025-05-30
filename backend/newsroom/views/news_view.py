import logging
from datetime import datetime

from django.http import HttpRequest, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from environs import Env

from ..data import NewsRepository
from ..schemas import News
from ..utils import jwt_required

env = Env()
env.read_env()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)


@method_decorator(jwt_required, name="dispatch")
class NewsView(View):
    def __init__(self):
        self.repository = NewsRepository()

    def _get_date(self, date: str):
        """expected in 'yyyy-mm-dd' patterns"""
        year, month, day = map(lambda x: int(x), date.split("-"))
        return datetime(year=year, month=month, day=day)

    def get(self, request: HttpRequest):
        logger.info(f"{request=}")
        # if not request.user.is_authenticated:
        #     return JsonResponse({"error": "User not authenticated"}, status=401)

        # username = request.user.username
        # email = request.user.email
        # first_name = request.user.first_name
        logger.info(request.GET)
        from_date = request.GET.get("fromDate", None)
        to_date = request.GET.get("toDate", None)
        keyword = request.GET.get("keyword", None)
        source_id = request.GET.get("sourceId", None)
        logger.info(f"{from_date=}, {to_date}, {keyword=}, {source_id=}")

        if from_date:
            from_date = self._get_date(from_date)
        if to_date:
            to_date = self._get_date(to_date)

        articles = self.repository.get_filtered_news(
            user_id=request.user_id,
            from_date=from_date,
            to_date=to_date,
            keyword=keyword,
            source_id=source_id,
        )

        # articles = [
        #     {
        #         "news_url": "https://apnews.com/article/south-carolina-shooting-little-river-7525cdaf1ffa5ac7b7e15c96fe74ecc0",
        #         "source_name": "BBC News",
        #         "title": "At least 11 hurt in South Carolina beach town shooting - AP News",
        #         "summary": "Authorities say at least 11 people were taken to hospitals after a shooting in a South Carolina beach town. Horry County Police did not give the conditions of anyone hurt or detail how they were injured in the incident, which happened about 9:30 p.m. Sunday i…",
        #         "published_at": "2025-05-26T11:51:00Z",
        #         "thumbnail_url": "https://dims.apnews.com/dims4/default/574d94d/2147483647/strip/true/crop/2593x1459+0+135/resize/1440x810!/quality/90/?url=https%3A%2F%2Fassets.apnews.com%2F5d%2Fec%2Fe2b517e513ffb6daf590461ad927%2Fcceeca456fd549a0a1f893b8eb346f53",
        #     }
        # ]
        return JsonResponse({"articles": self.__format_news(articles)}, status=200)

    def __format_news(self, articles: list[News]):
        return [
            {
                "news_url": article.news_url,
                "source_name": article.source_name,
                "title": article.title,
                "summary": article.summary,
                "published_at": article.publication_date,
                "thumbnail_url": article.thumbnail_url,
            }
            for article in articles
        ]
