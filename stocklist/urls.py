from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.PantryStocklist.as_view(), name='list'),
    path('add_stocklist/', views.add_stocklist, name='add_stocklist'),
    path('list/edit_stocklist/<slug:slug>', views.PantryStocklistEdit.as_view(), name='edit_stocklist'),
    path('spaces/', views.PantryStoragespaces.as_view(), name='spaces'),
    path('items/<slug:slug>', views.PantryStockitems.as_view(), name='items'),
]
