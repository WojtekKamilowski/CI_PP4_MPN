from django.shortcuts import render
from django.views import generic, View
from .models import Stocklist, Storagespace


def home(request):
    template_name = 'index.html'
    context = {}
    return render(request, template_name, context)


class PantryStocklist(generic.ListView):
    model = Stocklist
    template_name = 'list.html'

    def get_queryset(self):
        """
        Returns Stocklist of a specific user
        Based on CI-PP4-Meal-Planner
        """
        return Stocklist.objects.filter(user=self.request.user)


class PantryStoragespaces(generic.ListView):
    model = Storagespace
    template_name = 'spaces.html'
    paginate_by = 6

    # def storage_queryset(self):
    #     """
    #     Returns Storagespaces of a specific stocklist

    #     """       
    #     return Stocklist.objects.filter(stocklist=self.request.stocklist)
