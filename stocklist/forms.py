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
        fields = ['storage','item_name','expiry_date','remarks','min_temp','max_temp','quantity','uom']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = kwargs.get('stocklist')
        if user:
            fields['storage'].queryset = user.storage_set.all()
