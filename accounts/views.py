from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm

from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Accounts index page.")

def profile(request):
	return render(request, "accounts/profile.html")

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

