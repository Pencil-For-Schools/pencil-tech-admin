from unfold.admin import ModelAdmin
from django.utils.html import format_html
from django.urls import reverse
from django.contrib import admin
from admin_app.admin.configs import SuperuserOnlyAdminConfig


class PencilBoxLocationAdmin(SuperuserOnlyAdminConfig, ModelAdmin):
    list_display = ('name', 'inventory_items_link')

    def inventory_items_link(self, obj):
        count = obj.inventory_items.count()
        url = reverse('admin:admin_app_pencilboxlocationinventoryitem_changelist') + f'?pencil_box_location__id__exact={obj.id}'
        return format_html('<a href="{}">{} Inventory items</a>', url, count)

    inventory_items_link.short_description = 'Inventory Items'
