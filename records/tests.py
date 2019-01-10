from model_mommy import mommy

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.test import APIClient

from records.models import Record


class RecordServiceTestCase(TestCase):
    def setUp(self):
        self.user_1 = mommy.make(User, username="test_user")
        self.record_1 = mommy.make(Record, user=self.user_1,
                                   date="2018-01-02", weight=90)
        self.record_2 = mommy.make(Record, user=self.user_1,
                                   date="2018-01-03", weight=80)
        self.client = APIClient()

    def TearDown(self):
        pass

    def test_create_record(self):
        self.client.force_authenticate(self.user_1)
        url = reverse_lazy('api:app:records-list')
        payload = {
            "date": "2019-01-01",
            "weight": 80
        }
        response = self.client.post(url, data=payload)
        self.assertEqual(response.status_code, 201)
        record = Record.objects.get(user=self.user_1, date=payload["date"])
        self.assertEqual(record.weight, payload["weight"])

    def test_update_record(self):
        self.client.force_authenticate(self.user_1)
        url = reverse_lazy('api:app:records-list') + str(self.record_1.pk) + "/"
        payload = {
            "weight": 100
        }
        response = self.client.patch(url, data=payload)
        self.assertEqual(response.status_code, 200)
        record = Record.objects.get(pk=self.record_1.pk)
        self.assertEqual(record.weight, payload["weight"])

    def test_delete_record(self):
        self.client.force_authenticate(self.user_1)
        url = reverse_lazy('api:app:records-list') + str(self.record_2.pk) + "/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        with self.assertRaises(Record.DoesNotExist):
            record = Record.objects.get(pk=self.record_2.pk)
