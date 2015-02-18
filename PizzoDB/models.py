from django.db import models

class Project(models.Model):
	name = models.CharField(max_length=255)
	code = models.CharField(max_length=8)
	date_start = models.DateField(auto_now_add=False, auto_now=True)
	date_finish = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
	proposed_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	notes = models.TextField(blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.name

	def active(self):
		return not self.date_finish