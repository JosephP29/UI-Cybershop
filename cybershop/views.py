from django.shortcuts import render, redirect
from shop.models import Product


def index(request):
	productList = Product.objects.all()
	args = { 'products': productList }
	return render(request, 'index.html', args)