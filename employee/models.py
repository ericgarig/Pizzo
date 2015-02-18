from django.db import models

# Create your models here.

class Employee_Category(models.Model):
	name = models.CharField(max_length=255)
	abbr = models.CharField(max_length=5)
	cost = models.DecimalField(max_digits=7, decimal_places=2)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.name



class Employee(models.Model):
	employee_category = models.ForeignKey(Employee_Category, null=True)
	ssn = models.CharField(max_length=9, null=True)
	name_last = models.CharField(max_length=255, null=True)
	name_first = models.CharField(max_length=225, null=True)
	name_nick = models.CharField(max_length=255, null=True)
	date_birth = models.DateField(auto_now_add=False, auto_now=False, null=True)
	date_hire = models.DateField(auto_now_add=False, auto_now=True)
	date_fire = models.DateField(auto_now_add=False, auto_now=False, null=True)
	rate_hourly = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
	date_rate_increase = models.DateField(auto_now_add=False, auto_now=False)
	address_street = models.CharField(max_length=255, null=True)
	address_city = models.CharField(max_length=255, null=True)
	address_state = models.CharField(max_length=2, null=True)
	address_zip = models.CharField(max_length=5, null=True)
	phone_cell = models.CharField(max_length=10, null=True)
	phone_home = models.CharField(max_length=10, null=True)
	active = models.BooleanField(default=1)
	pancho = models.BooleanField(default=0)
	daboin = models.BooleanField(default=0)
	deleted = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return "%s, %s" % (self.name_last, self.name_first)

	def full_name(self):
		return "%s, %s ( %s )" % (self.name_last, self.name_first, self.name_nick)

	def full_address(self):
		if len(self.address_street):
			return "%s\n%s, %s %s" % (self.address_street, self.address_city, self.address_state, self.address_zip)
		else:
			return "No address specified"

	def phone_number(self, phone_string):
		if phone_string is not None and len(phone_string)==10:
			"""must be 'some' object whose length is 10"""
			return phone_string[:3] + '-' + phone_string[3:6] + '-' + phone_string[6:]
		else:
			return phone_string

	def phone_cell_display(self):
		return self.phone_number(self.phone_cell)

	def phone_home_display(self):
		return self.phone_number(self.phone_home)

	def ssn_display(self):
		if self.ssn is not None and len(self.ssn) == 9:
			return "XXX-XX-%s" % (self.ssn[5:])
		else:
			pass

	def rate_increase_date_display(self):
		if self.date_rate_increase is not None and self.date_rate_increase > self.date_hire:
			return self.date_rate_increase
		else:
			return "Initial rate"

	def nick_title(self):
		if self.name_nick is not None:
			_name = self.name_nick
		elif self.name_first is not None:
			_name = self.name_first
		else:
			_name = self.name_last
		if self.employee_category is not None:
			_cat = "( %s )" % self.employee_category.abbr
		else:
			_cat = ""
		return "%s %s" % (_name, _cat)