from django import forms
from .models import (
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
class CreateDanishpet(forms.ModelForm):
	class Meta:
		model = Danishpet
		fields = ['company_name','phone','address']
	
class CreateThinnapatti(forms.ModelForm):
	class Meta:
		model = Thinnapatti
		fields = ['company_name','phone','address']
		

class CreateThirupathi(forms.ModelForm):
	class Meta:
		model = Thirupathi
		fields = ['company_name','phone','address']


class CreateKaruppur(forms.ModelForm):
	class Meta:
		model = Karuppur
		fields = ['company_name','phone','address']


class CreateMuttampatti(forms.ModelForm):
	class Meta:
		model = Muttampatti
		fields = ['company_name','phone','address']

class CreateOmalur(forms.ModelForm):
	class Meta:
		model = Omalur
		fields = ['company_name','phone','address']

class CreateStealplant(forms.ModelForm):
	class Meta:
		model = Stealplant
		fields = ['company_name','phone','address']

class CreateTharamangalam(forms.ModelForm):
	class Meta:
		model = Tharamangalam
		fields = ['company_name','phone','address']

class CreateTholasampatti(forms.ModelForm):
	class Meta:
		model = Tholasampatti
		fields = ['company_name','phone','address']

class CreateElampillai(forms.ModelForm):
	class Meta:
		model = Elampillai
		fields = ['company_name','phone','address']

class CreateNeruppur(forms.ModelForm):
	class Meta:
		model = Neruppur
		fields = ['company_name','phone','address']

class CreateHogenakkal(forms.ModelForm):
	class Meta:
		model = Hogenakkal
		fields = ['company_name','phone','address']

class CreateMecheri(forms.ModelForm):
	class Meta:
		model = Mecheri
		fields = ['company_name','phone','address']

class CreateVanavasi(forms.ModelForm):
	class Meta:
		model = Vanavasi
		fields = ['company_name','phone','address']

class CreateMattur(forms.ModelForm):
	class Meta:
		model = Mattur
		fields = ['company_name','phone','address']

class CreateJalagai(forms.ModelForm):
	class Meta:
		model = Jalagai
		fields = ['company_name','phone','address']

class CreateEdappadi(forms.ModelForm):
	class Meta:
		model = Edappadi
		fields = ['company_name','phone','address']

class CreateSankari(forms.ModelForm):
	class Meta:
		model = Sankari
		fields = ['company_name','phone','address']

