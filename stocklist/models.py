from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# import cloudinary
# import cloudinary.uploader


class Stocklist(models.Model):
    name = models.CharField(max_length=150, default='Your Stock List')
    list_image = CloudinaryField('image', default='placeholder')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stock_list')
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-created_on']


class Storagespace(models.Model):
    storage_name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    stocklist = models.ForeignKey(Stocklist, on_delete=models.CASCADE, related_name='storage_space')
    storage_updated_on = models.DateTimeField(auto_now=True, null=True)
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
    item_name = models.CharField(max_length=50, unique=True)
    storage = models.ForeignKey(Storagespace, on_delete=models.CASCADE, related_name='stock_item', null=True)
    expiry_date = models.DateField(null=True, blank=False)
    remarks = models.TextField(blank=True)
    min_temp = models.IntegerField(default=-30)
    max_temp = models.IntegerField(default=30)
    quantity = models.IntegerField(default=1)
    uom = models.CharField(
        max_length=50,
        choices=UOM_CHOICES,
        default=PIECE,
    )

    class Meta:
        ordering: ['-expiry_date']

    def __str__(self):

        return self.item_name
