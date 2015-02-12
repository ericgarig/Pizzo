from django.contrib import admin
from .models import *

# Register your models here.
class AttendanceAdmin(admin.ModelAdmin):
	list_display = ['project', 'employee', 'date', 'hours']
	ordering = ('-date', 'employee')
	class Meta:
		model = Attendance

admin.site.register(Attendance, AttendanceAdmin)