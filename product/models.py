from django.db import models

# Create your models here.

class TaxAndProduct(models.Model):
	Name = models.CharField(max_length=255,null=True,blank=True)
	Desc = models.CharField(max_length=255,null=True,blank=True)
	Price = models.IntegerField(null=True,blank=True)
	TaxPer = models.FloatField(null=True,blank=True)
	TaxType =models.FloatField(null=True,blank=True)
	TaxAmount = models.CharField(max_length=255,null=True,blank=True)

	def __str__(self):
		return f"{self.Name}"



