from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Inventory, Material

# Create your views here.

class InventoryListView(generic.ListView):
	template_name='material/list.html'
	context_object_name = 'object_list'

	def get_queryset(self):
		return Inventory.objects.all


class InventoryDetailView(generic.DetailView):
	model = Inventory
	template_name = 'material/detail.html'







