from unfold.admin import ModelAdmin

from admin_app.admin.configs import SuperuserOnlyAdminConfig


class PencilBoxLocationInventoryItemAdmin(SuperuserOnlyAdminConfig, ModelAdmin):
    pass
