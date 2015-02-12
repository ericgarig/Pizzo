from django.contrib import admin
from .models import *

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
	class Meta:
		model = Employee


class Employee_CategoryAdmin(admin.ModelAdmin):
	class Meta:
		model = Employee_Category


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Employee_Category, Employee_CategoryAdmin)