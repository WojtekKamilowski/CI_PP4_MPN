from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
import datetime

# import cloudinary
# import cloudinary.uploader


class Stocklist(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True)
    list_image = CloudinaryField('image', default='placeholder')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='stock_list')
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Found on Stackoverflow
        """
        strtime = "".join(str(datetime.datetime.now()).split("."))
        string = "%s-%s" % (strtime[7:], self.name)
        self.slug = slugify(string)
        super(Stocklist, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on']


class Storagespace(models.Model):
    storage_name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True)
    stocklist = models.ForeignKey(Stocklist, on_delete=models.CASCADE, related_name='storage_space', null=True)
    storage_updated_on = models.DateTimeField(auto_now=True, null=True)
    temp = models.IntegerField(default=21)

    def __str__(self):
        return self.storage_name

    class Meta:
        # Found on Stackoverflow
        unique_together = 'stocklist', 'storage_name'

    def save(self, *args, **kwargs):
        """
        Found on Stackoverflow
        """
        strtime = "".join(str(datetime.datetime.now()).split("."))
        string = "%s-%s" % (strtime[7:], self.storage_name)
        self.slug = slugify(string)
        super(Storagespace, self).save(*args, **kwargs)

    def clean(self):
        """
        Found on Stackoverflow
        """
        self.storage_name = self.storage_name.capitalize()


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
    item_name = models.CharField(max_length=50)
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
        # Found on Stackoverflow
        unique_together = 'storage', 'item_name'

    def __str__(self):

        return self.item_name
    
    def clean(self):
        """
        Found on Stackoverflow
        """
        self.item_name = self.item_name.capitalize()
