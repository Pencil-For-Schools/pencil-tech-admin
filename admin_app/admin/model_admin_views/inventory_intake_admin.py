from unfold.admin import ModelAdmin

from admin_app.admin.configs import SuperuserOnlyAdminConfig


class InventoryIntakeAdmin(SuperuserOnlyAdminConfig, ModelAdmin):
    pass
