from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from accounts.forms import RegistrationForm
from django.contrib.auth import logout
from shop.models import BuyReceipt

from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Accounts index page.")

@login_required
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

@login_required
def prev_orders(request):
	prevOrders = BuyReceipt.objects.filter(owner=request.user)
	args = {'prevOrders': prevOrders}
	return render(request, 'accounts/prev_orders.html', args)

@login_required
def edit_profile(request):
	if request.method == 'POST':
		form = UserChangeForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('/accounts/profile')
	else:
		form = UserChangeForm(instance=request.user)
		args = {'form': form}
		return render(request, 'accounts/edit_profile.html', args)