from django.contrib import admin
from .models import Stocklist, Storagespace, Stockitem
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Stocklist)
class StocklistAdmin(SummernoteModelAdmin):

    list_display = ('name','created_on', 'updated_on')
    list_filter = ('created_on', 'updated_on')

@admin.register(Storagespace, Stockitem)
class StocklistAdmin(SummernoteModelAdmin):

    list_display = ('name',)
    search_fields = ('name',)
    summernote_fields = ('remarks')
