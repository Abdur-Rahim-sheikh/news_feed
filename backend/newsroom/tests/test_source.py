from newsroom.models import Source
from django.test import TestCase


class SourceModelTest(TestCase):
    def setUp(self):
        Source.objects.create(
            name="uv", url="www.example.com", language_code="py", country_code="un"
        )

    def test_object_created(self):
        data = Source.objects.all()
        self.assertEqual(len(data), 1)
