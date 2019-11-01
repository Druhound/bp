import datetime

from django.utils import timezone
from django.test import TestCase
from app.pages.models import Regulations


class RegulationsTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Regulations(datetime=time)
        self.assertEqual(future_question.was_published_recently(), False)