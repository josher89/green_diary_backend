from django.test import TestCase
from django.urls import reverse
from .models import Entry


class EntryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.entry = Entry.objects.create(text="This is a test")

    def test_model_content(self):
        self.assertEqual(self.entry.text, "This is a test")

    # def test_url_exists_at_correct_location(self):
    #     response = self.client.get("entry/")
    #     self.assertEqual(response.status_code, 200)
