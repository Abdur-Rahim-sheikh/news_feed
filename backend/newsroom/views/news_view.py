import logging
from datetime import datetime

from django.http import HttpRequest, JsonResponse
from django.views import View
from environs import Env

from ..data import NewsRepository
from ..schemas import News
from ..utils import jwt_required

env = Env()
env.read_env()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)


class NewsView(View):
    def __init__(self):
        self.repository = NewsRepository()

    def _get_date(self, date: str):
        """expected in 'yyyy-mm-dd' patterns"""
        year, month, day = map(lambda x: int(x), date.split("-"))
        return datetime(year=year, month=month, day=day)

    @jwt_required
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
        page_number = request.GET.get("page_number", 0)
        limit = request.GET.get("limit", 10)
        logger.info(f"{page_number=}, {limit=}")

        if from_date:
            from_date = self._get_date(from_date)
        if to_date:
            to_date = self._get_date(to_date)

        total_articles, articles = self.repository.get_filtered_news(
            user_id=request.user_id,
            from_date=from_date,
            to_date=to_date,
            keyword=keyword,
            source_id=source_id,
            page_number=page_number,
            limit=limit,
        )

        return JsonResponse(
            {
                "total_articles": total_articles,
                "articles": self.__format_news(articles),
            },
            status=200,
        )

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
