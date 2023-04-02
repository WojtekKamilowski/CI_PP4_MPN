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
        """
        return Stocklist.objects.filter(user=self.request.user)


class PantryStoragespaces(generic.ListView):
    model = Storagespace
    queryset = Storagespace.objects.filter(stocklist=True)
    template_name = 'spaces.html'
    paginate_by = 6
