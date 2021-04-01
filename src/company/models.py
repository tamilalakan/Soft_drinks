from django.db import models



# Create your models here.
class Danishpet(models.Model):
	company_name	= models.CharField(max_length=30)
	phone			= models.CharField(max_length=10,null=True)
	address			= models.TextField(max_length=100,null=True)


	def __str__(self):
		return self.company_name
	class Meta:
		verbose_name_plural = "Danishpet"


class Thinnapatti(models.Model):
	company_name	= models.CharField(max_length=30)
	phone			= models.CharField(max_length=10,null=True)
	address			= models.TextField(max_length=100,null=True)

	def __str__(self):
		return self.company_name

	class Meta:
		verbose_name_plural = "Thinnapatti"

class Thirupathi(models.Model):
	company_name	= models.CharField(max_length=30)
	phone			= models.CharField(max_length=10,null=True)
	address			= models.TextField(max_length=100,null=True)

	def __str__(self):
		return self.company_name
	class Meta:
		verbose_name_plural = "Thirupathi"

class Karuppur(models.Model):
	company_name	= models.CharField(max_length=30)
	phone			= models.CharField(max_length=10,null=True)
	address			= models.TextField(max_length=100,null=True)

	def __str__(self):
		return self.company_name
	class Meta:
		verbose_name_plural = "Karuppur"


class Muttampatti(models.Model):
	company_name	= models.CharField(max_length=30)
	phone			= models.CharField(max_length=10,null=True)
	address			= models.TextField(max_length=100,null=True)

	def __str__(self):
		return self.company_name
	class Meta:
		verbose_name_plural = "Muttampatti"

class Omalur(models.Model):
	company_name	= models.CharField(max_length=30)
	phone			= models.CharField(max_length=10,null=True)
	address			= models.TextField(max_length=100,null=True)

	def __str__(self):
		return self.company_name
	class Meta:
		verbose_name_plural = "Omalur"


class Stealplant(models.Model):
	company_name	= models.CharField(max_length=30)
	phone			= models.CharField(max_length=10,null=True)
	address			= models.TextField(max_length=100,null=True)

	def __str__(self):
		return self.company_name
	class Meta:
		verbose_name_plural = "Stealplant"

class Tharamangalam(models.Model):
	company_name	= models.CharField(max_length=30)
	phone			= models.CharField(max_length=10,null=True)
	address			= models.TextField(max_length=100,null=True)

	def __str__(self):
		return self.company_name
	class Meta:
		verbose_name_plural = "Tharamangalam"

class Tholasampatti(models.Model):
	company_name	= models.CharField(max_length=30)
	phone			= models.CharField(max_length=10,null=True)
	address			= models.TextField(max_length=100,null=True)

	def __str__(self):
		return self.company_name
	class Meta:
		verbose_name_plural = "Tholasampatti"

class Elampillai(models.Model):
	company_name	= models.CharField(max_length=30)
	phone			= models.CharField(max_length=10,null=True)
	address			= models.TextField(max_length=100,null=True)

	def __str__(self):
		return self.company_name
	class Meta:
		verbose_name_plural = "Elampillai"

class Neruppur(models.Model):
	company_name	= models.CharField(max_length=30)
	phone			= models.CharField(max_length=10,null=True)
	address			= models.TextField(max_length=100,null=True)

	def __str__(self):
		return self.company_name
	class Meta:
		verbose_name_plural = "Neruppur"

class Hogenakkal(models.Model):
	company_name	= models.CharField(max_length=30)
	phone			= models.CharField(max_length=10,null=True)
	address			= models.TextField(max_length=100,null=True)

	def __str__(self):
		return self.company_name
	class Meta:
		verbose_name_plural = "Hogenakkal"


class Mecheri(models.Model):
	company_name	= models.CharField(max_length=30)
	phone			= models.CharField(max_length=10,null=True)
	address			= models.TextField(max_length=100,null=True)

	def __str__(self):
		return self.company_name
	class Meta:
		verbose_name_plural = "Mecheri"

class Vanavasi(models.Model):
	company_name	= models.CharField(max_length=30)
	phone			= models.CharField(max_length=10,null=True)
	address			= models.TextField(max_length=100,null=True)

	def __str__(self):
		return self.company_name
	class Meta:
		verbose_name_plural = "Vanavasi"

class Mattur(models.Model):
	company_name	= models.CharField(max_length=30)
	phone			= models.CharField(max_length=10,null=True)
	address			= models.TextField(max_length=100,null=True)

	def __str__(self):
		return self.company_name
	class Meta:
		verbose_name_plural = "Mattur"

class Jalagai(models.Model):
	company_name	= models.CharField(max_length=30)
	phone			= models.CharField(max_length=10,null=True)
	address			= models.TextField(max_length=100,null=True)

	def __str__(self):
		return self.company_name
	class Meta:
		verbose_name_plural = "Jalagai"

class Edappadi(models.Model):
	company_name	= models.CharField(max_length=30)
	phone			= models.CharField(max_length=10,null=True)
	address			= models.TextField(max_length=100,null=True)

	def __str__(self):
		return self.company_name
	class Meta:
		verbose_name_plural = "Edappadi"

class Sankari(models.Model):
	company_name	= models.CharField(max_length=30)
	phone			= models.CharField(max_length=10,null=True)
	address			= models.TextField(max_length=100,null=True)

	def __str__(self):
		return self.company_name
	class Meta:
		verbose_name_plural = "Sankari"
