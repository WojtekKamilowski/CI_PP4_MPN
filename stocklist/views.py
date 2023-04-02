from django.shortcuts import render
from django.views import generic, View
from .models import Stocklist, Storagespace


def home(request):
    template_name = 'index.html'
    context = {}
    return render(request, template_name, context)


class PantryStocklist(generic.ListView):
    model = Stocklist
    queryset = Stocklist.objects.filter(user=1)
    template_name = 'list.html'


class PantryStoragespaces(generic.ListView):
    model = Storagespace
    queryset = Storagespace.objects.filter(stocklist)
    template_name = 'spaces.html'
    paginate_by = 6
