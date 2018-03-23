from django.contrib import admin
from shop.models import Product, PurchaseOrder
# Register your models here.
admin.site.register(Product)
admin.site.register(PurchaseOrder)