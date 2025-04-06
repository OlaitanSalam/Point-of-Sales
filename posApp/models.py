from datetime import datetime
from unicodedata import category
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=100)
    is_central = models.BooleanField(default=False, help_text="True if this is the central store.")

    def __str__(self):
        return self.name
    


class Products(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    name = models.TextField()
    price = models.FloatField(default=0)
    status = models.IntegerField(default=1) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.sku + " - " + self.name
    

# posApp/models.py (add this below your CustomUser model)
class Inventory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} at {self.store.name} - Qty: {self.quantity}"



class Sales(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True,
                              help_text="Store where the sale occurred")
    code = models.CharField(max_length=100)
    sub_total = models.FloatField(default=0)
    grand_total = models.FloatField(default=0)
    tendered_amount = models.FloatField(default=0)
    amount_change = models.FloatField(default=0)
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.code

class salesItems(models.Model):
    sale_id = models.ForeignKey(Sales,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    qty = models.FloatField(default=0)
    total = models.FloatField(default=0)


class CustomUser(AbstractUser):
    store = models.ForeignKey(Store, null=True, blank=True, on_delete=models.SET_NULL,
                              help_text="Assign user to a branch store. Leave empty for central store users.")
    is_superadmin = models.BooleanField(default=False,
        help_text="True for central store superusers with access to all stores.")

    def __str__(self):
        return self.username