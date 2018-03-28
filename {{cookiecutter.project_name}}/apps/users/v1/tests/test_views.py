from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from users.factories import UserFactory


class UserDetailViewTests(APITestCase):
    def _format_url(self, **kwargs):
        return reverse('v1:users:detail', kwargs=kwargs)

    def setUp(self):
        self.user = UserFactory(email='user@family.com', password='myweakpassword')
        self.client.force_login(self.user)

    def test_requires_auth(self):
        self.client.logout()
        response = self.client.get(self._format_url(pk=self.user.pk))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, {'detail': 'Authentication credentials were not provided.'})

    def test_get(self):
        """
        Test /users/:id
        """
        response = self.client.get(self._format_url(pk=self.user.pk))
        data = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data.get('email'), 'user@family.com')
        self.assertEqual(data.get('id'), 1)

    def test_get_me(self):
        """
        Test /users/me
        """
        self.client.force_login(self.user)
        response = self.client.get(self._format_url(pk='me'))
        data = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data.get('email'), 'user@family.com')
        self.assertEqual(data.get('id'), 1)

    def test_is_self(self):
        """
        Make sure a user can't retrieve information about other users
        """
        user = UserFactory()
        response = self.client.get(self._format_url(pk=user.id))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data, {'detail': 'You do not have permission to perform this action.'})
