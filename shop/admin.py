from django.contrib import admin
from shop.models import Product, PurchaseOrder, BuyReceipt

# Register your models here.
admin.site.register(Product)
admin.site.register(PurchaseOrder)
admin.site.register(BuyReceipt)