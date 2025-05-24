from dataclasses import dataclass


@dataclass
class Source:
    id: str
    name: str
    url: str
    language_code: str
    country_code: str
