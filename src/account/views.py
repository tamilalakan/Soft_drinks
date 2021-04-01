# Default
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.sessions.models import Session 
from django.http import JsonResponse
#Models
from .models import Employee, Sales, Home
from company.models import (
	Danishpet, 
	Thinnapatti, 
	Thirupathi, 
	Karuppur, 
	Muttampatti, 
	Omalur, 
	Stealplant, 
	Tharamangalam,
	Tholasampatti,
	Elampillai,
	Neruppur,
	Hogenakkal,
	Mecheri,
	Vanavasi,
	Mattur,
	Jalagai,
	Edappadi,
	Sankari,

)
# Forms

from .forms import CreateUserForm, CreateEmployee, CreateSales
from company.forms import (
	CreateDanishpet,
	CreateThinnapatti,
	CreateThirupathi,
	CreateKaruppur,
	CreateMuttampatti,
	CreateOmalur,
	CreateStealplant,
	CreateTharamangalam,
	CreateTholasampatti,
	CreateElampillai,
	CreateNeruppur,
	CreateHogenakkal,
	CreateMecheri,
	CreateVanavasi,
	CreateMattur,
	CreateJalagai,
	CreateEdappadi,
	CreateSankari,


	)

from geopy.geocoders import Nominatim
import requests


p_t = ['டேனிஷ்பேட்டை', 'தின்னபட்டி', 'திருப்பதி', 'கருப்பூர்', 'முத்தம்பட்டி', 'ஓமலூர்', 'இரும்பாலை', 'தாரமங்கலம்','தொளசம்பட்டி','இளம்பிள்ளை','நெருப்பூர்','ஒகேனகல்','மேச்சேரி','வனவாசி','மேட்டூர்','ஜலகை','எடப்பாடி','சங்ககிரி']
places = [Danishpet, Thinnapatti, Thirupathi, Karuppur,Muttampatti, Omalur, Stealplant, Tharamangalam, Tholasampatti, Elampillai, Neruppur, Hogenakkal, Mecheri, Vanavasi, Mattur, Jalagai, Edappadi, Sankari]
places_form = [CreateDanishpet,CreateThinnapatti,CreateThirupathi,CreateKaruppur,CreateMuttampatti,CreateOmalur,CreateStealplant,CreateTharamangalam,CreateTholasampatti,CreateElampillai,CreateNeruppur,CreateHogenakkal,CreateMecheri,CreateVanavasi,CreateMattur,CreateJalagai,CreateEdappadi,CreateSankari]
numbers=['0','1','2','3','4','5','6','7','8','9']


def home(request):

	# geolocator = Nominatim(user_agent='MyGeocoder')
	# location = geolocator.geocode("11.6431946, 78.1508203").raw
	# print(location)
	l = []
	if (not request.user.is_superuser) and request.user.is_authenticated:
		obj = Employee.objects.get(username=request.user)
		if obj.daily_address is not None:
			s = (obj.daily_address).split(' ')
			s =s[2:len(s)-1]
			for i in s:
				l.append(p_t[int(i)-1])

	if not request.user.is_authenticated:
		return redirect('login')

	return render(request,'account/home.html',{'datas':l,'places':p_t})



def register(request):
	error= ""
	if request.method == 'POST':

		form = CreateUserForm(request.POST)
		form1 = CreateEmployee(request.POST)
		if form.is_valid() and form1.is_valid():
			form.save()
			form1.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(request,username=username, password=raw_password)

			if user is not None:
				login(request, user)
				return redirect('home')
		else:
			error = "error"
	else:
		form = CreateUserForm()
	return render (request,'account/register.html',{'form':form,'error':error})


def loginPage(request):
	error = ""
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password1')
		user = authenticate(request,username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			error = "error"

	return render(request,'account/login.html',{'error':error})

def logoutpage(request):
	logout(request)
	return redirect('home')

def forms(request):
	error=''

	if request.method == 'POST' and (not request.user.is_superuser):
		form = CreateSales(request.POST)
		print(form)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			error = 'error'
			form = CreateSales()
	elif request.method == 'POST' and request.user.is_superuser:
		val = ''
		obj = Employee.objects.get(username=request.POST.get('employee_name'))
		for i,j in (request.POST).items():
			val += i + ' '
		obj.daily_address = val
		obj.save()

		return redirect('home')


	return render(request, 'account/forms.html',{'error':error,'pla':p_t})

def details(request,id):
	if id[0] in numbers:
		obj = places[int(id)-1].objects.all()
		typ = 0
	else:
		obj = Sales.objects.filter(companyname=id)
		typ = 1
	return render(request, 'account/details.html',{'obj':obj,'typ':typ})


def chart_view(request,id):
	label, data = [], []
	context = {'01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0}
	if id in numbers:
		obj = places[int(id)-1].objects.all()
		for i in obj:
			for j in (Sales.objects.filter(companyname=i)):
					s = str(j.date)
					s = s[5:7]
					context[str(s)] += j.bottles
	
	elif id == 'all':
		context = {}
		for i in range(len(places)):
			total_amount = 0
			company_places = places[i].objects.all()
			for j in company_places:
				company_nam = Sales.objects.filter(companyname=j)
				for k in company_nam:
					total_amount += k.amount 
			context[p_t[i]] = total_amount

	else:
		values = Sales.objects.filter(companyname=id)
		for i in values:
			s = str(i.date)
			s = s[5:7]
			context[str(s)] +=i.bottles

	for key, val in context.items():
		label.append(key)
		data.append(val)

	return render(request, 'account/chart.html',{'label':label,'data':data})


def addcompany(request,id):
	# if request.method == 'POST':
	
	if request.method == 'POST':
		form = places_form[int(id)-1](request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = CreateDanishpet()

	return render(request, 'account/addcompany.html',{'places':p_t,'form':form})

def account(request):
	user_value = Employee.objects.get(username=request.user)
	sales = Sales.objects.all()
	if request.method == 'POST':
		user_value.phonenumber = request.POST.get('phonenumber')
		user_value.save()
		return redirect('home')


	return render(request, 'account/acc.html',{'user':user_value,'sales':sales}) 
