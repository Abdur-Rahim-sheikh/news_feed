from dataclasses import dataclass
from datetime import datetime


@dataclass
class News:
    source_url: str
    title: str
    source_name: str
    summary: str
    publication_date: datetime
    thumbnail: str
