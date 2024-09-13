from unfold.admin import ModelAdmin

from admin_app.admin.configs import SuperuserOnlyAdminConfig


class PencilBoxLocationAdmin(SuperuserOnlyAdminConfig, ModelAdmin):
    list_display = ["name", "address1", "city", "state", "zip"]
    list_filter = ["city", "state"]
