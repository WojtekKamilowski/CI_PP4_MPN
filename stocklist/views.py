from django.shortcuts import render
from django.views import generic, View
from .models import Stocklist, Storagespace


def home(request):
    template_name = 'index.html'
    context = {}
    return render(request, template_name, context)


class PantryStocklist(generic.ListView):
    model = Stocklist
    queryset = Stocklist.objects.all()
    template_name = 'list.html'


class PantryStoragespaces(generic.ListView):
    model = Storagespace
    queryset = Storagespace.objects.all()
    template_name = 'spaces.html'
