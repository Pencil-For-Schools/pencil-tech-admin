from unfold.admin import ModelAdmin

from admin_app.admin.configs import SuperuserOnlyAdminConfig


class ScheduleItemAdmin(SuperuserOnlyAdminConfig, ModelAdmin):
    pass
