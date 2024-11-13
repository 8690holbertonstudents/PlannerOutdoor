from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase


class UserAPITests(APITestCase):
    """
    Testing for users:
        Create a new user,
        Login existing user,
        Delete existing user.
        Recover user password.
    """

    def test_register_user(self):
        url = reverse("users-register")
        data = {"username": "testuser",
                "password": "Test>012",
                "email": "testuser@maildrop.cc",
                "address": "toronto"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get_user_model().objects.count(), 1)

    def test_login_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            password="Test>012",
            email="testuser@maildrop.cc",
            address="toronto")
        url = reverse("token_obtain_pair")
        data = {"username": "testuser",
                "password": "Test>012"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_delete_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            password="Test>012",
            email="testuser@maildrop.cc",
            address="toronto")
        self.client.force_authenticate(user=user)
        url = reverse("users-delete-account", args=[user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)

    def test_recover_password(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            password="Test>012",
            email="testuser@maildrop.cc",
            address="toronto"
        )
        url = reverse("users-recover-password")
        data = {
            "username": "testuser",
            "email": "testuser@maildrop.cc"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("message", response.data)
