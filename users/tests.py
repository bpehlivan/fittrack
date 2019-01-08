from model_mommy import mommy

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.test import APIClient


class UserViewSetTestCase(TestCase):
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
        response = self.client.post(reverse_lazy("api:auth:users-list"), data)
        self.assertEqual(response.status_code, 201)
        created_user = User.objects.get_by_natural_key(data["username"])
        self.assertEqual(created_user.first_name, data["first_name"])

    def test_perform_update(self):
        data = {
            "first_name": "test_name"
        }
        response = self.client.patch(
            "/api-v1/auth/users/{0}/".format(self.user_1.pk),
            data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["first_name"], "test_name")

    def test_perform_destroy(self):
        response = self.client.delete(
            "/api-v1/auth/users/{0}/".format(self.user_1.pk),
            format='json')
        self.assertEqual(response.status_code, 204)
        deleted_user = User.objects.get_by_natural_key(self.user_1.username)
        self.assertFalse(deleted_user.is_active)
