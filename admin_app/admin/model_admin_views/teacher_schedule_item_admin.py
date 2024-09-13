from unfold.admin import ModelAdmin

from admin_app.admin.configs import SuperuserOnlyAdminConfig


class TeacherScheduleItemAdmin(SuperuserOnlyAdminConfig, ModelAdmin):
    pass
