from django.db import models

from PizzoDB.models import Project

# Create your models here.

class Inventory(models.Model):
	name = models.CharField(max_length=255)
	category = models.CharField(max_length=255, blank=True, null=True)
	subtype = models.CharField(max_length=255, blank=True, null=True)
	description = models.CharField(max_length=255, blank=True, null=True, default='NULL')
	cost = models.DecimalField(max_digits=7, decimal_places=2)
	created = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True, null=True)

	def __str__(self):
		return self.name



class Material(models.Model):
	inventory = models.ForeignKey(Inventory, null=True)
	project = models.ForeignKey('PizzoDB.Project')
	date = models.DateField(auto_now_add=True, auto_now=False)
	cost = models.CharField(max_length=9)
	quantity = models.DecimalField(max_digits=7, decimal_places=2)
	notes = models.CharField(max_length=255, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True, null=True)

	def __str__(self):
		return "%s for  %s ( %s )" % (self.inventory, self.project, self.date)

	def full_name(self):
		return "%s, %s ( %s )" % (self.name_last, self.name_first, self.name_nick)

	def material_name(self):
		return self.inventory.name


