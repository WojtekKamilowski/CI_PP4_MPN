from django import forms
from .models import Stocklist, Storagespace


class StocklistForm(forms.ModelForm):
    class Meta:
        model = Stocklist
        fields = ['name']


class StorageForm(forms.ModelForm):
    class Meta:
        model = Storagespace
        fields = ['storage_name','temp']
