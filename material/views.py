from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Inventory, Material

# Inventory

class InventoryListView(generic.ListView):
	template_name='material/inventory_list.html'
	context_object_name = 'inventory'

	def get_queryset(self):
		return Inventory.objects.all


class InventoryDetailView(generic.DetailView):
	model = Inventory
	template_name = 'material/inventory_detail.html'




# Material

class MaterialListView(generic.ListView):
	template_name='material/list.html'
	context_object_name = 'material'

	def get_queryset(self):
		return Material.objects.all


class MaterialDetailView(generic.DetailView):
	model = Material
	template_name = 'material/detail.html'



