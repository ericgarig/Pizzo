from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Attendance

class AttendanceListView(generic.ListView):
	template_name = 'attendance/list.html'
	context_object_name = 'attendance_list'

	def get_queryset(self):
		return Attendance.objects.all()

class AttendanceDetailView(generic.DetailView):
	model = Attendance
	template_name = 'attendance/detail.html'