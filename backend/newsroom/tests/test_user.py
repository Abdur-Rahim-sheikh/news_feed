from django.test import TestCase
from newsroom.models import User


class TestUser(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="abir", email="admin@admin.com")

    def test_get_full_name(self):
        self.assertEqual(self.user.username, "abir")
