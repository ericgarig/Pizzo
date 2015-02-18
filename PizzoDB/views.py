from django.views import generic

from .models import Project
from attendance.models import Attendance
from material.models import Material


def active_projects(self):
	return Project.objects.filter(date_finish__isnull=True)


class ProjectListView(generic.ListView):
	template_name = 'PizzoDB/list.html'
	context_object_name = 'object_list'

	def get_queryset(self):
		return active_projects(self)


class ProjectDetailView(generic.DetailView):
	model = Project
	template_name = 'PizzoDB/detail.html'




