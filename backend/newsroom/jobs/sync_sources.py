from datetime import datetime

from environs import Env
from newsapi import NewsApiClient

from newsroom.models import Source as sourcedb
from newsroom.schemas import Source

env = Env()
env.read_env()
news_api = NewsApiClient(api_key=env.str("NEWS_API"))


def sync_sources():
    # scheduler running twice at each interval
    # handle this later seperating the schedule call
    # from original call 'runserver'
    print(f"{datetime.now().date()=} running simple job", flush=True)
    db = sourcedb.objects.all().order_by("id")
    sources = news_api.get_sources()

    print(db, flush=True)
