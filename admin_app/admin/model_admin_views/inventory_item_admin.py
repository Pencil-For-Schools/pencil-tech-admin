from unfold.admin import ModelAdmin

from admin_app.admin.configs import SuperuserOnlyAdminConfig


class InventoryItemAdmin(SuperuserOnlyAdminConfig, ModelAdmin):
    pass
