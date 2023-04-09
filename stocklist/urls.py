from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.PantryStocklist.as_view(), name='list'),
    path('addstocklist/', views.add_stocklist, name='addstocklist')
    path('spaces/', views.PantryStoragespaces.as_view(), name='spaces'),
    path('items/<slug:slug>', views.PantryStockitems.as_view(), name='items'),
]
