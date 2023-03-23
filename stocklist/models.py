from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Stocklist(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stock_list')

class Storagespace(models.Model):
    name = models.CharField(max_length=150, unique=True)
    stocklist = models.ForeignKey(Stocklist, on_delete=models.CASCADE, related_name='storage_space')
    temp = models.IntegerField(default=21)

PIECE = 'PC'
LITRE = 'L'
KILOGRAM = 'KG'
BOTTLE = 'BOTTLE'
CUP = 'CUP'
PACK = 'PACK'

UOM_CHOICES = [
        (PIECE, 'pc'),
        (LITRE, 'L'),
        (KILOGRAM, 'kg'),
        (BOTTLE, 'bottle'),
        (CUP, 'cup'),
        (PACK, 'pack'),
    ]

class Stockitem(models.Model):
    name = models.CharField(max_length=50, unique=True)
    storage = models.ManyToManyField(Storagespace)
    expiry_date = models.DateField(null=True, blank=True)
    remarks = models.TextField()
    product_image = CloudinaryField('image', default='placeholder')
    min_temp = models.IntegerField(default=-30)
    max_temp = models.IntegerField(default= 30)
    quantity = models.IntegerField(default= 1)
    uom = models.CharField(
        max_length=50,
        choices=UOM_CHOICES,
        default=PIECE,
    )

    class Meta:
        ordering: ['-expiry_date']
    
    def __str__(self):
        return self.name
