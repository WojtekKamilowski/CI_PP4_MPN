from django.shortcuts import render, get_object_or_404
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


class PantryStockitems(View):

    def get(self, request, slug, *args, **kwargs):
        """
        Returns items of a specific storagespace
        """
        queryset = Stockitem.objects.select_related('storage').filter(storage__slug=slug)
        stock_item = queryset
        storage_spaces = Storagespace.objects.select_related('stocklist').filter(stocklist__user=self.request.user)
        storage_space = get_object_or_404(storage_spaces, slug=slug)

        return render (
            request,
            'items.html',
            {
                'storage_space': storage_space,
                'stock_item': stock_item,
            },
        )


def add_stocklist(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = StocklistForm()
    context = {
        'form': form
    }
    return render(request, 'list/add_stocklist.html', context)
