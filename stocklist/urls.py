from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.PantryStocklist.as_view(), name='list'),
    path('add_stocklist/', views.PantryStocklist.add_stocklist, name='add_stocklist'),
    path('list/edit_stocklist/<slug:slug>', views.PantryStocklist.edit_stocklist, name='edit_stocklist'),
    path('spaces/', views.PantryStoragespaces.as_view(), name='spaces'),
    path('spaces/edit_storage/<slug:slug>', views.PantryStoragespaces.edit_storagespace, name='edit_storage'),
    path('add_storage/', views.PantryStoragespaces.add_storagespace, name='add_storage'),
    path('items/<slug:slug>', views.PantryStockitems.as_view(), name='items'),
    path('items/<slug:slug>/add_item/', views.PantryStockitems.item_create, name='add_item'),
    path('items/edit_item/<slug:slug>', views.PantryStockitems.edit_stockitem, name='edit_item'),
]
