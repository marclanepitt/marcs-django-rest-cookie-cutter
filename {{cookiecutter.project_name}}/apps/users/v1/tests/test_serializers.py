from django.utils import timezone
from rest_framework.test import APITestCase

from users.factories import UserFactory
from users.v1 import serializers


class UserDetailSerializerTests(APITestCase):
    def setUp(self):
        self.serializer_cls = serializers.UserDetailSerializer
        self.date_joined = timezone.now()
        self.user = UserFactory(first_name='John', last_name='Doe', date_joined=self.date_joined)

    def test_output(self):
        expected = {
            'id': 1,
            'first_name': 'John',
            'last_name': 'Doe',
            'full_name': 'John Doe',
            'email': 'user0@family.com',
            'username': 'user0@family.com',
            'last_login': None,
            'is_active': True,
            'date_joined': self.date_joined.isoformat()[:-6] + 'Z',
            'userprofile': None
        }
        serializer = self.serializer_cls(self.user)
        self.assertDictEqual(serializer.data, expected)
