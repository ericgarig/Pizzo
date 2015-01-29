from django.contrib import admin
from .models import *

# Register your models here.
class AttendanceAdmin(admin.ModelAdmin):
	class Meta:
		model = Attendance



class EmployeeAdmin(admin.ModelAdmin):
	class Meta:
		model = Employee



class Employee_CategoryAdmin(admin.ModelAdmin):
	class Meta:
		model = Employee_Category



class ProjectAdmin(admin.ModelAdmin):
	list_display = ['code', 'name', 'date_start']
	ordering = ('-code',)
	class Meta:
		model = Project



admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Employee_Category, Employee_CategoryAdmin)
admin.site.register(Project, ProjectAdmin)