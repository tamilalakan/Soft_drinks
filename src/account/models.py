from django.db import models
# Create your models here.


class Employee(models.Model):
	username 		= models.CharField(max_length=30)
	phonenumber		= models.CharField(max_length=10, null=True, blank=True)
	daily_address	= models.CharField(max_length=100, null=True,blank=True)
	password1 		= models.CharField(max_length=20) 
	password2 		= models.CharField(max_length=20)

	def __str__(self):
		return self.username

class Sales(models.Model):
	employee_name = models.CharField(max_length=30)
	companyname = models.CharField(max_length=20)
	bottles = models.IntegerField()
	original_amount = models.FloatField()
	amount = models.FloatField()
	date = models.DateField()
	location = models.CharField(max_length=80,null=True)

	def __str__(self):
		return self.companyname
	
	class Meta:
		verbose_name_plural = "Sales"

class Home(models.Model):
	name 	= models.CharField(max_length=32)
	picture = models.ImageField(upload_to='home')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Home"