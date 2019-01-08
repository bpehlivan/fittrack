from model_mommy import mommy

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.test import APIClient


class AccountViewTestCase(TestCase):
    def setUp(self):
        self.user_1 = mommy.make(User)
        self.client = APIClient()

    def tearDown(self):
        pass

    def test_perform_create(self):
        data = {
            "first_name": "foo",
            "last_name": "bar",
            "email": "foo@bar.com",
            "username": "test_user",
            "password": "test_password"
        }
        response = self.client.post(reverse_lazy("api:auth:account"), data)
        self.assertEqual(response.status_code, 201)
        created_user = User.objects.get_by_natural_key(data["username"])
        self.assertEqual(created_user.first_name, data["first_name"])

    def test_perform_update(self):
        data = {
            "first_name": "test_name"
        }
        self.client.force_authenticate(self.user_1)
        response = self.client.patch("/api-v1/auth/account/",
                                     data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["first_name"], "test_name")

    def test_perform_destroy(self):
        self.client.force_authenticate(self.user_1)
        response = self.client.delete("/api-v1/auth/account/", format='json')
        self.assertEqual(response.status_code, 204)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get_by_natural_key(self.user_1.username)
