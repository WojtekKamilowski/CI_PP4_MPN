from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.PantryStocklist.as_view(), name='list'),
]
