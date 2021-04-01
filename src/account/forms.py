from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee, Sales

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username' ,'password1', 'password2']

class CreateEmployee(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ['username', 'password1', 'password2']


class CreateSales(forms.ModelForm):
	class Meta:
		model = Sales
		fields = ['employee_name','companyname','bottles','original_amount','amount','date','location']