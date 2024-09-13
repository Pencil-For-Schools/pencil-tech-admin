from unfold.admin import ModelAdmin

from admin_app.admin.configs import SuperuserOnlyAdminConfig


class InventoryIntakeAdmin(SuperuserOnlyAdminConfig, ModelAdmin):
    list_display = ["inventory_item", "qty_donated", "intake_type", "updated_at"]
    list_filter = ["intake_type"]
