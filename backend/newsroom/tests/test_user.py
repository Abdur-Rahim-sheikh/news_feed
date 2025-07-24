from django.test import TestCase
from newsroom.models import User as userdb
from ..schemas import User


class TestUser(TestCase):
    def setUp(self):
        self.user = userdb.objects.create(
            username="abir",
            email="admin@admin.com",
            first_name="abir",
            last_name="sheikh",
        )

    def test_username(self):
        self.assertEqual(self.user.username, "abir")

    def test_full_name(self):
        user = User(
            username=self.user.username,
            email=self.user.email,
            first_name=self.user.first_name,
            last_name=self.user.last_name,
            country_codes=self.user.country_codes,
            source_ids=self.user.source_ids,
            keywords=self.user.keywords,
            password=self.user.password,
            id=self.user.id,
        )
        self.assertEqual(user.full_name, "abir sheikh")
