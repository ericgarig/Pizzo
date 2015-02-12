from django.contrib import admin
from .models import *

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
	list_display = ['code', 'name', 'date_start']
	ordering = ('-code',)
	class Meta:
		model = Project


admin.site.register(Project, ProjectAdmin)