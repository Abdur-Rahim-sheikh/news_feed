import logging

from environs import Env
from newsapi import NewsApiClient

from newsroom.models import News as dbnews
from newsroom.models import Source as sourcedb
from newsroom.models import User as userdb

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

env = Env()
env.read_env()
news_api = NewsApiClient(api_key=env.str("NEWS_API"))


def sync_news():
    users = userdb.objects.all()
    source_instance = sourcedb.objects.all()

    sources = {source.name: source.id for source in source_instance}
    countries = set()
    sources = set()
    for user in users:
        countries.update(user.countries)
        sources.update(user.sources)

    articles = {}
    for country in countries:
        # fmt: off
        # later test if reponse comes less than totalResults
        response = news_api.get_top_headlines(
            country=country,
            page_size=100 
        )
        # fmt: on

        if response["status"] != "ok":
            continue
        total = response["totalResults"]
        found = len(response["articles"])
        logger.info(f"{country=}, {total=}, {found=}")
        if total != found:
            logger.warning(f"{total=}!={found=}")

        for article in response["articles"]:
            src_id = None
            if article["source"]["id"]:
                src_id = article["source"]["id"]
            elif article["source"]["name"] and article["source"]["name"] in sources:
                src_id = sources[article["source"]["name"]]

            if not all(
                (src_id, article["url"], article["title"], article["description"])
            ):
                continue
            entry = dbnews(
                news_url=article["url"],
                country_code=country,
                source_id=src_id,
                title=article["title"],
                summary=article["description"],
                publication_date=article["publishedAt"],
                thumbnail_url=article["urlToImage"],
            )
            articles[article["url"]] = entry

    newss = dbnews.objects.all()
    exclude = []
    for row in newss:
        if row.news_url in articles:
            articles.pop(row.news_url)
        else:
            exclude.append(row.news_url)

    include = articles.values()

    dbnews.objects.bulk_create(include)
    dbnews.objects.filter(news_url__in=include).delete()

    logger.info(f"new article {len(include)=}, {len(exclude)=}")
