from django.contrib import admin
from .models import *

# Register your models here.
class InventoryAdmin(admin.ModelAdmin):
	class Meta:
		model = Inventory


class MaterialAdmin(admin.ModelAdmin):
	class Meta:
		model = Material


admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Material, MaterialAdmin)