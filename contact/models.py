# Imports
# 3rd party:
from django.db import models
from django.contrib.auth.models import User

# From CI_PP4_the_diplomat

# Model for the contact item in the database


class Contact(models.Model):
    """
    Contact model class
    """

    message_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, default="")
    message = models.TextField()

    class Meta:
        ordering = ["created_date"]

    def __str__(self):
        return self.name
