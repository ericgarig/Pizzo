from django.db import models
from django.db.models import Count
	

class Vacation_Day(models.Model):
	employee = models.ForeignKey('employee.Employee')
	date_used = models.DateField(auto_now_add=False, auto_now=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s took a day on %s" % (self.employee, self.date_used)

	def vacation_for_employee(self):
		return Vacation_Day.objects.annotate(total_days=count('date_used'))