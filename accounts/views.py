from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Accounts index page.")

def profile(request):
	return render(request, "accounts/profile.html")