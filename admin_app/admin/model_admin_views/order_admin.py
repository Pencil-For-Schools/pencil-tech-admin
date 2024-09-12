from unfold.admin import ModelAdmin

from admin_app.admin.configs import SuperuserOnlyAdminConfig


class OrderAdmin(SuperuserOnlyAdminConfig, ModelAdmin):
    pass
