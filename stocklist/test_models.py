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
            user=self.user,
            )
        self.assertEqual(stocklist.name, 'Test Stocklist')
        self.assertTrue(stocklist.user)
    
    def test_new_storagespace(self):
        """
        Test to create a new storagespace
        Checks for the storage_name, stocklist & temp
        """
        # From Stackoverflow
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

        stocklist = Stocklist.objects.create(
            name='Test Stocklist',
            user=self.user,
            )
        
        storagespace = Storagespace.objects.create(
            storage_name='Test Storagespace',
            stocklist=stocklist,
            temp=21
            )
        self.assertEqual(storagespace.storage_name,'Test Storagespace')
        self.assertTrue(storagespace.stocklist,'Test Stocklist')
        self.assertEqual(storagespace.temp, 21)
