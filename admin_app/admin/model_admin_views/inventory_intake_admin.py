from admin_app.admin.configs import SuperuserOnlyAdminConfig
from unfold.admin import ModelAdmin

class InventoryIntakeAdmin(SuperuserOnlyAdminConfig, ModelAdmin):
    pass
