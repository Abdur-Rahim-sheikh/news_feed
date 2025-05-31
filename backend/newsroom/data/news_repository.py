import logging
from datetime import datetime, timedelta

from django.db.models import Q

from ..models import User
from ..schemas import News

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class NewsRepository:
    def get_filtered_news(
        self,
        user_id: int,
        from_date: datetime = None,
        to_date: datetime = None,
        keyword: str = None,
        source_id: str = None,
        page_number: int = 0,
        limit: int = 10,
    ) -> tuple[int, list[News]]:
        news = User.objects.get(pk=user_id).news_set.all()
        if from_date:
            news = news.filter(publication_date__gte=from_date)
        if to_date:
            news = news.filter(publication_date__lte=to_date + timedelta(days=1))
        if source_id:
            news = news.filter(source_id=source_id)
        if keyword:
            news = news.filter(
                Q(title__icontains=keyword) | Q(summary__icontains=keyword)
            )
        total_articles = news.count()
        offset = page_number * limit
        news = news[offset : offset + limit]
        articles = []
        for row in news:
            article = News(
                news_url=row.news_url,
                title=row.title,
                country_code=row.country_code,
                source_name=row.source.name,
                summary=row.summary,
                publication_date=row.publication_date,
                thumbnail_url=row.thumbnail_url,
            )
            articles.append(article)

        return total_articles, articles
