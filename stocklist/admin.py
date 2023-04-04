from django.contrib import admin
from .models import Stocklist, Storagespace, Stockitem
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Stocklist)
class StocklistAdmin(SummernoteModelAdmin):

    list_display = ('name', 'created_on', 'updated_on')
    list_filter = ('created_on', 'updated_on')


@admin.register(Storagespace)
class StocklistAdmin(SummernoteModelAdmin):

    list_display = ('storage_name',)
    search_fields = ('storage_name',)


@admin.register(Stockitem)
class StocklistAdmin(SummernoteModelAdmin):

    list_display = ('item_name',)
    search_fields = ('item_name',)
    summernote_fields = ('remarks')
