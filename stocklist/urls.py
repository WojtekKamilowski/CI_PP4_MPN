from . import views
from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("list/", views.PantryStocklist.as_view(), name="list"),
    path("add_stocklist/", views.PantryStocklist.add_stocklist,
         name="add_stocklist"),
    path(
        "list/edit_stocklist/<slug:slug>",
        views.PantryStocklist.edit_stocklist,
        name="edit_stocklist",
    ),
    path(
        "list/delete_stocklist/<slug:slug>",
        views.PantryStocklist.delete_stocklist,
        name="delete_list",
    ),
    path("spaces/", views.PantryStoragespaces.as_view(), name="spaces"),
    path(
        "spaces/edit_storage/<slug:slug>",
        views.PantryStoragespaces.edit_storagespace,
        name="edit_storage",
    ),
    path(
        "spaces/delete_storage/<slug:slug>",
        views.PantryStoragespaces.delete_storagespace,
        name="delete_storage",
    ),
    path(
        "add_storage/", views.PantryStoragespaces.add_storagespace,
        name="add_storage"
    ),
    path("items/<slug:slug>", views.PantryStockitems.as_view(), name="items"),
    path(
        "items/<slug:slug>/add_item/",
        views.PantryStockitems.item_create,
        name="add_item",
    ),
    path(
        "items/edit_item/<slug:slug>",
        views.PantryStockitems.edit_stockitem,
        name="edit_item",
    ),
    path(
        "items/delete_item/<slug:slug>",
        views.PantryStockitems.delete_stockitem,
        name="delete_item",
    ),
]
