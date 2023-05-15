# Imports
# 3rd party:
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
# Internal:
from .forms import ContactForm

# From CI_PP4_the_diplomat


def get_user_instance(request):
    """
    Retrieves user details if logged in
    """
    user_username = request.user.username
    user_email = request.user.email
    user = User.objects.filter(email=user_email, username=user_username).first()
    return user


class ContactMessage(View):
    """
    Displays form for the user to contact the admin.
    If user is registered inserts the user email  & name into the
    relevant fields.
    """

    template_name = "contact/contact.html"
    success_message = "Your message has been sent."

    def get(self, request, *args, **kwargs):
        """
        Retrieves users email & name and inputs into relevant input
        """
        if request.user.is_authenticated:
            email = request.user.email
            name = request.user.username
            form = ContactForm(initial={"email": email, "name": name})
        else:
            form = ContactForm()
        return render(request, "contact/contact.html", {"form": form})

    def post(self, request):
        """
        Checks if the details are in valid format
        and then posts to database.
        """
        form = ContactForm(data=request.POST)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            messages.success(request, "Your message has been sent")
            return render(request, "contact/received.html")

        return render(request, "contact/contact.html", {"form": form})
