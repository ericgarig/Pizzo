from django.db import models

class Project(models.Model):
	name = models.CharField(max_length=255)
	code = models.CharField(max_length=8)
	date_start = models.DateField()
	proposed_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	notes = models.TextField(blank=True, null=True)
	active = models.BooleanField(default=0)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.name



class Employee_Category(models.Model):
	name = models.CharField(max_length=255)
	abbr = models.CharField(max_length=5)
	cost = models.DecimalField(max_digits=7, decimal_places=2)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.name



class Employee(models.Model):
	employee_category_id = models.ForeignKey(Employee_Category, null=True)
	ssn = models.CharField(max_length=9, unique=True)
	name_last = models.CharField(max_length=255)
	name_first = models.CharField(max_length=225)
	name_nick = models.CharField(max_length=255)
	date_birth = models.DateField(auto_now_add=False, auto_now=False, null=True)
	date_hire = models.DateField(auto_now_add=False, auto_now=True)
	date_fire = models.DateField(auto_now_add=False, auto_now=False, null=True)
	rate_hourly = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
	rate_increate_date = models.DateField(auto_now_add=False, auto_now=False)
	address_street = models.CharField(max_length=255)
	address_city = models.CharField(max_length=255)
	address_state = models.CharField(max_length=2)
	address_zip = models.CharField(max_length=5)
	phone_cell = models.CharField(max_length=10)
	phone_home = models.CharField(max_length=10)
	is_pancho = models.BooleanField(default=0)
	is_temp_layoff = models.BooleanField(default=0)
	deleted = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.name_last & ', ' & self.name_first



class Attendance(models.Model):
	employee_id = models.ForeignKey(Employee)
	project_id = models.ForeignKey(Project)
	date = models.DateField()
	hours = models.FloatField(default=8)
	cost_per_day = models.FloatField()
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return 



