from django.shortcuts import render, redirect
from shop.models import Product
from django.db.models import Count, Min, Sum, Avg


def index(request):
	productList = Product.objects.filter(category='Food')[:4]
	productList1 = Product.objects.filter(category='Sports')[:4]
	productList2 = Product.objects.filter(category='Entertainment')[:4]
	productList3 = Product.objects.filter(category='Electronics')[:4]
	deal = Product.objects.order_by('price').first()
	args = { 'products': productList, 'products1': productList1, 'products2': productList2, 'products3': productList3, 'deal': deal }
	return render(request, 'index.html', args)

def help(request):
	return render(request, 'help.html')