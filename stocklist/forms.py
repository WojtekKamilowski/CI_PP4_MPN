from django import forms
from .models import Stocklist


class StocklistForm(forms.ModelForm):
    class Meta:
        model = Stocklist
        fields = ['name', 'list_image']
        