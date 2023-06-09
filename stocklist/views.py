# Imports
# 3rd party:
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
import datetime
# Internal:
from .models import Stocklist, Storagespace, Stockitem
from .forms import StocklistForm, StorageForm, ItemForm


def home(request):
    """
    Displays home page
    """
    template_name = "stocklist/index.html"
    context = {}
    return render(request, template_name, context)


class PantryStocklist(generic.ListView):
    model = Stocklist
    template_name = "stocklist/list.html"

    def get_queryset(self):
        """
        Returns stocklist of a specific user
        Based on CI-PP4-Meal-Planner
        """
        return Stocklist.objects.filter(user=self.request.user)

    def add_stocklist(request):
        """
        Displays form to create a new stocklist
        Inspired by CI_PP4_the_diplomat
        """
        form = StocklistForm(data=request.POST)
        if form.is_valid():
            stocklist = form.save(commit=False)
            stocklist.user = request.user
            stocklist.save()
            messages.success(request, "Stocklist added!")
            return redirect("list")

        return render(request, "stocklist/add_stocklist.html", {"form": form})

    def edit_stocklist(request, slug):
        """
        View to edit stocklist
        Inspired by HelloDjango
        """
        stocklist = get_object_or_404(Stocklist, slug=slug)
        if request.method == "POST":
            form = StocklistForm(request.POST, instance=stocklist)
            if form.is_valid():
                stocklist.user = request.user
                form.save()
                messages.success(request, "Stocklist edit completed!")
                return redirect("list")
        form = StocklistForm(instance=stocklist)
        context = {"form": form}
        return render(request, "stocklist/edit_stocklist.html", context)

    def delete_stocklist(request, slug):
        """
        Delete stocklist with option to confirm
        """
        stocklist = get_object_or_404(Stocklist, slug=slug)
        if request.method == "POST":
            stocklist.delete()
            messages.success(request, "Your stocklist deleted!")
            return redirect("list")
        return render(request, "stocklist/delete_list.html",
                      {"stocklist": stocklist})


class PantryStoragespaces(generic.ListView):
    model = Storagespace
    template_name = "stocklist/spaces.html"
    paginate_by = 6

    def get_queryset(self):
        """
        Returns list of storagespaces of a specific stocklist
        """
        return (
            Storagespace.objects.select_related("stocklist")
            .filter(stocklist__user=self.request.user)
            .order_by("storage_name")
        )

    def add_storagespace(request):
        """
        Displays form to create a new storagespace
        """
        if request.method == "POST":
            form = StorageForm(request.POST, request.FILES)
            if form.is_valid():
                storage_space = form.save(commit=False)
                stocklist = get_object_or_404(Stocklist, user=request.user)
                storage_space.stocklist = stocklist
                storagespace = form.save()
                messages.success(request, "A new storagespace has been added!")
                return redirect("spaces")
        else:
            form = StorageForm()

        template = "stocklist/add_storage.html"
        context = {
            "form": form,
        }

        return render(request, template, context)

    def edit_storagespace(request, slug):
        """
        Displays form to edit storagespace
        Inspired by HelloDjango
        """
        storagespace = get_object_or_404(Storagespace, slug=slug)

        if request.method == "POST":
            form = StorageForm(request.POST, instance=storagespace)
            if form.is_valid():
                form.save()
                messages.success(request, "Storagespace edit completed!")
                return redirect("spaces")
        form = StorageForm(instance=storagespace)
        context = {"form": form}
        return render(request, "stocklist/edit_storage.html", context)

    def delete_storagespace(request, slug):
        """
        View to delete storagespace with prior confirmation
        Based on Stackoverflow & CI_PP4_the_diplomat
        """
        storagespace = get_object_or_404(Storagespace, slug=slug)

        if request.method == "POST":
            storagespace.delete()
            messages.success(request, "Storagespace deleted!")
            return redirect("spaces")

        return render(
            request, "stocklist/delete_storage.html",
                     {"storagespace": storagespace}
        )


class PantryStockitems(View):
    def get(self, request, slug, *args, **kwargs):
        """
        Returns items in a specific storagespace
        """
        queryset = (
            Stockitem.objects.select_related("storage")
            .filter(storage__slug=slug)
            .order_by("expiry_date")
        )
        stock_item = queryset
        str_spaces = Storagespace.objects.select_related("stocklist").filter(
            stocklist__user=self.request.user
        )
        storage_space = get_object_or_404(str_spaces, slug=slug)

        return render(
            request,
            "stocklist/items.html",
            {
                "storage_space": storage_space,
                "stock_item": stock_item,
            },
        )

    def item_create(request, slug, *args, **kwargs):
        """
        Displays form to create a new item
        Found on Stackoverflow
        """
        str_spaces = Storagespace.objects.select_related("stocklist").filter(
            stocklist__user=request.user
        )
        storage_space = get_object_or_404(str_spaces, slug=slug)

        if request.method == "POST":
            form = ItemForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                messages.success(request, "A new stockitem has been added!")
                return redirect(reverse("items", args=[slug]))
        else:
            form = ItemForm()
            str_select = Storagespace.objects.select_related(
                    "stocklist"
                ).filter(stocklist__user=request.user)
            form.fields["storage"].queryset = str_select
        template = "stocklist/add_item.html"
        context = {
            "form": form,
        }

        return render(request, template, context)

    def edit_stockitem(request, slug, *args, **kwargs):
        """
        View to edit an item
        """
        stockitem = get_object_or_404(Stockitem, slug=slug)
        if request.method == "POST":
            form = ItemForm(request.POST, instance=stockitem)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                messages.success(request, "Stockitem edit completed!")
                return redirect("spaces")
        else:
            form = ItemForm(instance=stockitem)
            str_select = Storagespace.objects.select_related(
                "stocklist"
            ).filter(stocklist__user=request.user)
            form.fields["storage"].queryset = str_select
        context = {"form": form}
        return render(request, "stocklist/edit_item.html", context)

    def delete_stockitem(request, slug, *args, **kwargs):
        """
        View for deleting a stockitem after user confirmed
        Based on Stackoverflow & CI_PP4_the_diplomat
        """
        stock_item = get_object_or_404(Stockitem, slug=slug)

        if request.method == "POST":
            stock_item.delete()
            messages.success(request, "Item deleted!")
            return redirect("spaces")

        return render(request, "stocklist/delete_item.html",
                      {"stock_item": stock_item})
