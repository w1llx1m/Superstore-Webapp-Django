from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CreateUserForm(UserCreationForm):
	username = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Username..."}))
	email = forms.CharField(required=True, widget=forms.EmailInput(attrs={"placeholder": "enter your e-mail"}))
	password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"placeholder": "password"}))
	password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"placeholder": "confirm your password"}))
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']