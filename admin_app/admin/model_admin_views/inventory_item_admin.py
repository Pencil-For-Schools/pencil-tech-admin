from admin_app.admin.configs import SuperuserOnlyAdminConfig
from unfold.admin import ModelAdmin

class InventoryItemAdmin(SuperuserOnlyAdminConfig, ModelAdmin):
    pass
