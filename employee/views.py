# from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Employee
from attendance.models import Attendance

# Create your views here.

class EmployeeListView(generic.ListView):
	template_name='employee/list.html'
	context_object_name = 'object_list'

	def get_queryset(self):
		return Employee.objects.filter(active=1).order_by('name_nick')


class EmployeeDetailView(generic.DetailView):
	model = Employee
	template_name = 'employee/detail.html'







