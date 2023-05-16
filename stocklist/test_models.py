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
        self.assertTrue(storagespace.stocklist)
        self.assertEqual(storagespace.temp, 21)

    def test_new_stockitem(self):
        """
        Test to create a new stockitem
        Checks for the item_name, storage, expiry_date, remarks
        min_temp, max_temp, quantity, uom
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

        PIECE='pc'
        stockitem = Stockitem.objects.create(
            item_name='Test Item',
            storage=storagespace,
            expiry_date='2024-01-01',
            remarks='Test remarks',
            min_temp=-30,
            max_temp=30,
            quantity=1,
            uom=PIECE,
            )
        self.assertEqual(stockitem.item_name,'Test Item')
        self.assertTrue(stockitem.storage)
        self.assertEqual(stockitem.expiry_date, '2024-01-01')
        self.assertEqual(stockitem.remarks, 'Test remarks')
        self.assertEqual(stockitem.min_temp, -30)
        self.assertEqual(stockitem.max_temp, 30)
        self.assertEqual(stockitem.quantity, 1)
        self.assertEqual(stockitem.uom, PIECE)






