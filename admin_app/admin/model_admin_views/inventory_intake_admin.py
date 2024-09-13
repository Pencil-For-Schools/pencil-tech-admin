from unfold.admin import ModelAdmin
from django.utils.translation import gettext_lazy as _
from unfold.decorators import display
from admin_app.admin.configs import SuperuserOnlyAdminConfig
from admin_app.models import PencilBoxLocationInventoryItem, IntakeType, InventoryItem
from datetime import datetime


class InventoryIntakeAdmin(SuperuserOnlyAdminConfig, ModelAdmin):
    
    def save_model(self, request, obj, form, change):
        
        super().save_model(request, obj, form, change)
        try:
            location_item = PencilBoxLocationInventoryItem.objects.get(pencil_box_location=obj.pencil_box_location, inventory_item=obj.inventory_item)
            location_item.in_stock += obj.qty_donated
            location_item.save()
        except PencilBoxLocationInventoryItem.DoesNotExist:
            PencilBoxLocationInventoryItem.objects.create(
                inventory_item = obj.inventory_item,
                pencil_box_location = obj.pencil_box_location,
                bin_number = 0,
                low_stock = 0,
                max_amt = 0,
                sold = 0,
                in_stock = obj.qty_donated,
                last_audited = datetime.now(),
                archived = False
                )
