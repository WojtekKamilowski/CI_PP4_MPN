from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Stocklist(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User,)

class Storagespace(models.Model):
    name = models.CharField(max_length=150, unique=True)
    stocklist = models.ForeignKey(Stocklist)
    temp = models.IntegerField(default=21)

UOM_CHOICES = [
        (PIECES, 'pcs'),
        (LITRES, 'L'),   
    ]

class Stockitem(models.Model):
    name = models.CharField(max_length=50, unique=True)
    storage = models.ManyToManyField(Storagespace, related_name='name')
    expiry_date = models.DateField(null=True, blank=True)
    remarks = models.TextField()
    product_image = CloudinaryField('image', default='placeholder')
    min_temp = models.IntegerField(default=-30)
    max_temp = models.IntegerField(default= 30)
    quantity = models.IntegerField(default= 1)
    uom = models.CharField(
        choices= UOM_CHOICES,
        default=PIECES,
    )