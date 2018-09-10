from django.contrib import admin
from .models import Product, Order
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','brand','pname','price','inventory','description','imageurl']
    list_editable = ['brand', 'pname', 'price', 'inventory', 'description', 'imageurl']
    list_per_page = 20
admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','product', 'first_name', 'last_name', 'dateordered', 'ordertotal', 'address_line_1', 'address_line_2', 'city', 'state', 'zipcode']
    list_editable = ['product', 'first_name', 'last_name', 'dateordered', 'ordertotal', 'address_line_1', 'address_line_2', 'city', 'state', 'zipcode']
    list_per_page = 20
admin.site.register(Order, OrderAdmin)
