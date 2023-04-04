from django.shortcuts import render
from django.views import generic, View
from .models import Stocklist, Storagespace, Stockitem


def home(request):
    template_name = 'index.html'
    context = {}
    return render(request, template_name, context)


class PantryStocklist(generic.ListView):
    model = Stocklist
    template_name = 'list.html'

    def get_queryset(self):
        """
        Returns stocklist of a specific user
        Based on CI-PP4-Meal-Planner
        """
        return Stocklist.objects.filter(user=self.request.user)


class PantryStoragespaces(generic.ListView):
    model = Storagespace
    template_name = 'spaces.html'
    paginate_by = 6

    def get_queryset(self):
        """
        Returns list of storagespaces of a specific stocklist
        """       
        return Storagespace.objects.select_related('stocklist').filter(stocklist__user=self.request.user)


class PantryStockitems(generic.ListView):
    model = Stockitem
    template_name = 'items.html'
    paginate_by = 10
    

    def get_queryset(self):
        """
        Returns items of a specific storagespace
        """ 
        return Stockitem.objects.select_related('storage').filter(storage__stocklist__user=self.request.user)
