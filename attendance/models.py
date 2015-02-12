from django.db import models

# from PizzoDB.models import Project
# from employee.models import Employee


class Attendance(models.Model):
	project = models.ForeignKey('PizzoDB.Project')
	employee = models.ForeignKey('employee.Employee')
	date = models.DateField(auto_now_add=False, auto_now=True)
	hours = models.DecimalField(max_digits=4, decimal_places=2, default=8)
	cost_daily = models.DecimalField(max_digits=7, decimal_places=2, null=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	deleted = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

	def __str__(self):
		return "%s - %s (%s)" % (str(self.project), str(self.employee), str(self.date))

