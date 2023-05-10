from django import forms
from .models import Stocklist, Storagespace, Stockitem


class StocklistForm(forms.ModelForm):
    class Meta:
        model = Stocklist
        fields = ["name"]


class StorageForm(forms.ModelForm):
    class Meta:
        model = Storagespace
        fields = ["storage_name", "temp"]


class DateInput(forms.DateInput):
    """
    Datepicker found on Stackoverflow
    """

    input_type = "date"


class ItemForm(forms.ModelForm):
    class Meta:
        model = Stockitem
        fields = [
            "item_name",
            "expiry_date",
            "storage",
            "remarks",
            "min_temp",
            "max_temp",
            "quantity",
            "uom",
        ]
        # Datepicker found on Stackoverflow
        widgets = {
            "expiry_date": DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = kwargs.get("stocklist")
        if user:
            fields["storage"].queryset = user.storage_set.all()
