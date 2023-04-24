from django import forms
from .models import Stocklist, Storagespace, Stockitem


class StocklistForm(forms.ModelForm):
    class Meta:
        model = Stocklist
        fields = ['name']


class StorageForm(forms.ModelForm):
    class Meta:
        model = Storagespace
        fields = ['storage_name','temp']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Stockitem
        fields = ['item_name','expiry_date','remarks','min_temp','max_temp','quantity','uom']

    

        