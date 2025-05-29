from dataclasses import dataclass


@dataclass
class User:
    username: str
    email: str
    first_name: str
    last_name: str
    country_codes: list
    source_ids: list
    keywords: list

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
