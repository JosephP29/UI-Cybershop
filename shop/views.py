from django.shortcuts import render
from shop.models import Product

# Create your views here.
def index(request):
	productList = Product.objects.all()
	args = { 'products': productList }
	return render(request, 'shop/index.html', args)