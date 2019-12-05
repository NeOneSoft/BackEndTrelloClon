from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class TokenAuthTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='test@gmail.com', password='123456')

    def test_get_token(self):
        result = self.client.post('/api/token/', {'username': 'test_user', 'password': '123456'})
        print(result.status_code)
        print(result.data)
        assert result.status_code == 200
        assert 'access' in result.data

    def test_valid_token(self):
        result = self.client.post('/api/token/', {'username': 'test_user', 'password': '123456'})
        token = result.data['access']

        user_result = self.client.get('/api/v1/users/', HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        assert user_result.status_code == 200
        assert user_result.data['count'] == 1

