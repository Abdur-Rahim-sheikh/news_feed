import logging
from collections import defaultdict

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

    sources_dict = {source.name: source.id for source in source_instance}
    sources_keys = set(sources_dict.values())
    countries = defaultdict(list)
    sources = defaultdict(list)
    for user in users:
        for country in user.country_codes:
            countries[country].append(user)
        for source_id in user.source_ids:
            sources[source_id].append(user)

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
            elif (
                article["source"]["name"] and article["source"]["name"] in sources_dict
            ):
                src_id = sources_dict[article["source"]["name"]]

            if not all(
                (
                    src_id in sources_keys,
                    article["url"],
                    article["title"],
                    article["description"],
                )
            ):
                logger.info(
                    f"Failed! {article["url"]=}, {src_id=}, {article['source']}"
                )
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

    existing_urls = set(row.news_url for row in dbnews.objects.all())
    exclude = []
    for url in existing_urls:
        if url in articles:
            articles.pop(url)
        else:
            exclude.append(url)

    include = articles.values()

    dbnews.objects.filter(news_url__in=exclude).delete()
    dbnews.objects.bulk_create(include)

    newss = dbnews.objects.all()
    for article in newss:
        country_users = countries[article.country_code]
        source_users = sources[article.source.id]
        article.users.set(country_users + source_users)

    logger.info(f"new article {len(include)=}, {len(exclude)=}")
