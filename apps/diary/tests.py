from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class DiaryTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_diary_activity_list(self):
        response = self.client.get(reverse('diary-activity-create'))
        self.assertEqual(200, response.status_code)

    def test_diary_food_list(self):
        response = self.client.get(reverse('diary-food-create'))
        self.assertEqual(200, response.status_code)