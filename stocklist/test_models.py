from django.test import TestCase
from django.contrib.auth.models import User
from .models import Stocklist, Storagespace, Stockitem


class TestModels(TestCase):

    def test_new_stocklist(self):
        """
        Test to create a new stocklist
        Checks the name and user
        """

        # From Stackoverflow
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

        stocklist = Stocklist.objects.create(
            name='Test Stocklist',
            user=self.user
            )
        self.assertEqual(stocklist.name, 'Test Stocklist')
        self.assertTrue(stocklist.user)

