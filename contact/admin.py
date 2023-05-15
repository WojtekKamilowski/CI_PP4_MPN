# Imports
# 3rd party:
from django.contrib import admin
# Internal:
from .models import Contact

# From CI_PP4_the_diplomat


# Contact information in the admin panel to review messages
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_filter = ("user", "name", "email", "created_date")
    list_display = ("message_id", "name", "message", "created_date")

    search_fields = ["name"]
    list_filter = ("created_date",)
