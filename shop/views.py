from django.shortcuts import render, redirect
from shop.models import Product, PurchaseOrder
from shop.forms import BuyProductForm

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

def buy_product(request, title):
	product = Product.objects.get(title=title)
	user = request.user

	if request.method == 'POST':
		buy_form = BuyProductForm(request.POST)
		if buy_form.is_valid():
			buy_form = buy_form.save(commit=False)
			buy_form.owner = request.user
			buy_form.product = product.title
			buy_form.price = product.price
			buy_form.total = buy_form.price * buy_form.units
			buy_form.save()

			PurchaseOrder.objects.create(owner=request.user, units=buy_form.units, title=title, price=buy_form.total)
			return redirect('accounts/profile')
	else:
		buy_form = BuyProductForm()
		args = {'form': buy_form, 'product': product}
		return render(request, 'shop/buy_product.html', args)

	return render(request, 'shop/buy_product.html')

def searchresults(request):
	if request.method == 'GET':
		searchProduct = request.GET.get('searchProd')
		if searchProduct:
			status = Product.objects.filter(title__icontains=searchProduct)
			return render(request, "index.html", {"products": status})
		else:
			return render(request, "index.html", {})
	else:
		return render(request, "index.html", {}) 

def cat(request):
	if request.method == 'GET':
		search_category = request.GET.get('searchCat')
		if search_category:
			if search_category == "All":
				status = Product.objects.all()
				return render(request, "index.html", {"products": status})
			status = Product.objects.filter(category__icontains=search_category)
			return render(request, "index.html", {"products": status})
		else:
			return render(request, "index.html", {})
	else:
		return render(request, "index.html", {}) 