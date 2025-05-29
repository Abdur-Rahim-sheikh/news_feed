from django.db import IntegrityError

from ..models import User as userdb
from ..schemas import User


class UserRepository:
    def add_user(
        self, first_name: str, last_name: str, username: str, email: str, password: str
    ) -> User:
        try:
            user = userdb.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
            )
        except IntegrityError as e:
            raise IntegrityError(f"user could not be created {e}")
        user = User(
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            country_codes=user.country_codes,
            source_ids=user.source_ids,
            keywords=user.keywords,
        )
        return user
