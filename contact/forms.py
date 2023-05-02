# Imports
# 3rd party:
from django import forms
# Internal:
from .models import Contact

# From CI_PP4_the_diplomat

# The contact form for the user to send a message to the business


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "message")
