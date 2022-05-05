from django.shortcuts import render

# Create your views here.

def home(request, *args, **kwargs):
	context = {}
	return render(request, 'home.html', context)


def login_view(request, *args, **kwargs):
	context = {}
	return render(request, 'login.html', context)