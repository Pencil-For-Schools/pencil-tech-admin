from unfold.admin import ModelAdmin
from django.utils.translation import gettext_lazy as _
from unfold.decorators import display
from admin_app.admin.configs import SuperuserOnlyAdminConfig
from admin_app.models import PencilBoxLocationInventoryItem, IntakeType, InventoryItem


class InventoryIntakeAdmin(SuperuserOnlyAdminConfig, ModelAdmin):
    
    def save_model(self, request, obj, form, change):
        
        super().save_model(request, obj, form, change)
        if obj.intake_type.name == "Add":
            try:
                location_item = PencilBoxLocationInventoryItem.objects.get(pencil_box_location=obj.pencil_box_location, inventory_item=obj.inventory_item)
            except Exception:
                PencilBoxLocationInventoryItem.create(
                    
                )
            location_item.in_stock = obj.qty_donated
            location_item.save()
