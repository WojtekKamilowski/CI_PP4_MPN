from django.contrib import admin
from .models import Stocklist, Storagespace, Stockitem
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Stocklist, Storagespace, Stockitem)
class StocklistAdmin(SummernoteModelAdmin):

    summernote_fields = ('remarks')
