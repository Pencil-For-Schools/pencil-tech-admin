from admin_app.admin.configs import SuperuserOnlyAdminConfig
from unfold.admin import ModelAdmin

class PencilBoxLocationAdmin(SuperuserOnlyAdminConfig, ModelAdmin):
    pass
