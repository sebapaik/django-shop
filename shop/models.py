from django.db import models
from django.utils import timezone
from django.urls import reverse

class Product(models.Model):
    id = models.AutoField(primary_key = True)
    brand = models.CharField(max_length = 300)
    pname = models.CharField(max_length = 300)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField()
    description = models.TextField()
    imageurl = models.CharField(max_length = 1000)

    def __str__(self):
        return f"{self.brand} {self.pname}"


class Order(models.Model):
    id = models.AutoField(primary_key = True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    dateordered = models.DateTimeField(default=timezone.now)
    ordertotal = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    address_line_1 = models.CharField(max_length = 300, null=True, blank=True)
    address_line_2 = models.CharField(max_length = 300, null=True, blank=True)
    city = models.CharField(max_length = 300, null=True, blank=True)
    state = models.CharField(max_length = 300, null=True, blank=True)
    zipcode = models.CharField(max_length = 300, null=True, blank=True)

    def __str__(self):
        return f"Order #{self.id}"
