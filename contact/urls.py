# Imports
# 3rd party:
from django.urls import path

# Internal:
from contact import views

# From CI_PP4_the_diplomat

# Urls for the contact page
urlpatterns = [
    path("contact/", views.ContactMessage.as_view(), name="contact"),
]
