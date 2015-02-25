# from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Vacation_Day

class VacationDayListView(generic.ListView):
	template_name = 'vacation_day/list.html'
	context_object_name = 'vacation_day_list'

	def get_queryset(self):
		return Vacation_Day.objects.all()

class VacationDayDetailView(generic.DetailView):
	model = Vacation_Day
	template_name = 'vacation_day/detail.html'