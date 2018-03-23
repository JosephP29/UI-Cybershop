from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	price = models.PositiveIntegerField()
	image = models.ImageField(upload_to='product_image', blank=True)

	def __str__(self):
		return self.title

class PurchaseOrder(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	product_type = models.CharField(max_length=200)
	price = models.PositiveIntegerField()
	units = models.PositiveIntegerField()
	date_bought = models.DateTimeField(auto_now=True)

	def __str__(self):
		string = str(self.owner) + " - " + self.product
		return string