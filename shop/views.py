from django.shortcuts import render
from shop.models import Product

# Create your views here.
def index(request):
	productList = Product.objects.all()
	args = { 'products': productList }
	return render(request, 'shop/index.html', args)

def productdetail(request, title):
	user = request.user
	product = Product.objects.get(title=title)
	args = {
		'product': product
	}
	return render(request, 'shop/productdetail.html', args)