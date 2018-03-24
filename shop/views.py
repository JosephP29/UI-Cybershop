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
			if buy_form.units > 0:
				buy_form.owner = request.user
				buy_form.product = product.title
				buy_form.price = product.price
				buy_form.total = buy_form.price * buy_form.units
				buy_form.save()

				PurchaseOrder.objects.create(owner=request.user, units=buy_form.units, title=title, price=buy_form.total)
				return redirect('/accounts/prev_orders')
			else:
				buy_form = BuyProductForm()
				args = {'form': buy_form, 'product': product}
				return render(request, 'shop/buy_product.html', args)

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
			status1 = Product.objects.filter(category__icontains=searchProduct)
			status2 = Product.objects.filter(description__icontains=searchProduct)
			s = status | status1 | status2
			return render(request, "shop/searchresults.html", {"products": s})
		else:
			productList = Product.objects.filter(category='Food')[:4]
			productList1 = Product.objects.filter(category='Sports')[:4]
			productList2 = Product.objects.filter(category='Entertainment')[:4]
			productList3 = Product.objects.filter(category='Electronics')[:4]
			deal = Product.objects.order_by('price').first()
			args = { 'products': productList, 'products1': productList1, 'products2': productList2, 'products3': productList3, 'deal': deal }
			return render(request, "index.html", args)
	else:
		productList = Product.objects.filter(category='Food')[:4]
		productList1 = Product.objects.filter(category='Sports')[:4]
		productList2 = Product.objects.filter(category='Entertainment')[:4]
		productList3 = Product.objects.filter(category='Electronics')[:4]
		deal = Product.objects.order_by('price').first()
		args = { 'products': productList, 'products1': productList1, 'products2': productList2, 'products3': productList3, 'deal': deal }
		return render(request, "index.html", args) 

def cat(request):
	if request.method == 'GET':
		search_category = request.GET.get('searchCat')
		if search_category:
			if search_category == "All":
				status = Product.objects.all()
			else:
				status = Product.objects.filter(category__icontains=search_category)
			return render(request, "shop/searchresults.html", {"products": status})
		else:
			return render(request, "index.html", {})
	else:
		return render(request, "index.html", {}) 