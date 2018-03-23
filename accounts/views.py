from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm
from django.contrib.auth import logout

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
	print("hello")
	logout(request)
	return redirect(request, 'accounts/login.html')

