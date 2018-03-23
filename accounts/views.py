from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm
from django.contrib.auth import logout
from shop.models import BuyReceipt

from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Accounts index page.")

def profile(request):
	user = request.user
	args = { 'user': request.user }
	return render(request, "accounts/profile.html", args)

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('../../')
	else:
		form = RegistrationForm()
		args = {'form': form}
		return render(request, 'accounts/reg_form.html', args)

def logout(request):
	logout(request)
	return redirect(request, 'accounts/login.html')

def prev_orders(request):
	prevOrders = BuyReceipt.objects.filter(owner=request.user)
	print(prevOrders)
	args = {'prevOrders': prevOrders}
	return render(request, 'accounts/prev_orders.html', args)