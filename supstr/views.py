from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm

# Create your views here.

def home(request, *args, **kwargs):
	context = {}
	return render(request, 'home.html', context)


def sing_up_view(request, *args, **kwargs):
	form = CreateUserForm()
	context = {'form': form}
	if request.method == "POST":
		print(request.objects.get('inputEmail4'))
	return render(request, 'singup.html', context)