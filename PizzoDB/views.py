from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Project
from Pizzo import views

class ProjectListView(ListView):

	model = Project

	def get_context_data(self, **kwargs):
		context = super(ProjectListView, self).get_context_data(**kwargs)
		return Project.objects.order_by('-code')

def active_projects(request):
	return Project.objects.filter(active=1)

def index(request):
	project_list = active_projects(request)
	context = {'project_list': project_list}
	return render(request, 'PizzoDB/home.html', context)

def detail(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	return render(request, 'PizzoDB/project.html', {'project':project})





# class IndexView(generic.ListView):
# 	template_name = 'polls/index.html'
# 	context_object_name = 'latest_question_list'

# 	def get_queryset(self):
# 		"""Return the last five published quesitons"""
# 		return Question.objects.order_by('-pub_date')[:5]