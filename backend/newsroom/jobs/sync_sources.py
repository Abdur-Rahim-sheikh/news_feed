import logging
from datetime import datetime

from environs import Env
from newsapi import NewsApiClient

from newsroom.models import Source as sourcedb

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

env = Env()
env.read_env()
news_api = NewsApiClient(api_key=env.str("NEWS_API"))


def sync_sources():
    # scheduler running twice at each interval
    # handle this later seperating the schedule call
    # from original call 'runserver'
    db = sourcedb.objects.all().order_by("id")
    response = news_api.get_sources()
    sources = {
        src["id"]: sourcedb(
            id=src["id"],
            name=src["name"],
            url=src["url"],
            language_code=src["language"],
            country_code=src["country"],
        )
        for src in response["sources"]
        if src["id"]
    }
    exclude = []
    for row in db:
        if row.id in sources:
            sources.pop(row.id)
        else:
            exclude.append(row.id)

    include = sources.values()
    sourcedb.objects.filter(pk__in=exclude).delete()
    sourcedb.objects.bulk_create(include)
    logger.info(f"new {exclude=}, {include=}")
