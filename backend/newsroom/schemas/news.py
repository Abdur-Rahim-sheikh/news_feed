from dataclasses import dataclass
from datetime import datetime


@dataclass
class News:
    news_url: str
    title: str
    country_code: str
    source_name: str
    summary: str
    publication_date: datetime
    thumbnail_url: str
