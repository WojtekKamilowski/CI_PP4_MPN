from django.test import TestCase
from .models import Stocklist, Storagespace, Stockitem


class TestModels(TestCase):

    def test_new_stocklist(self):
        stocklist = Stocklist.objects.create(
            name='Test Stocklist',
        )
        