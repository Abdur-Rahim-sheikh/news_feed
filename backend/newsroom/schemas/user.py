from dataclasses import dataclass

from django.contrib.auth.hashers import check_password


@dataclass
class User:
    username: str
    email: str
    first_name: str
    last_name: str
    country_codes: list
    source_ids: list
    keywords: list
    password: str = None

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def verify_password(self, password: str) -> bool:
        if not self.password:
            return False
        return check_password(password, self.password)
