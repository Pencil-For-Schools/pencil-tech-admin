from unfold.admin import ModelAdmin

from admin_app.admin.configs import SuperuserOnlyAdminConfig
from unfold.contrib.filters.admin import RangeDateFilter, RangeDateTimeFilter

class ScheduleItemAdmin(SuperuserOnlyAdminConfig, ModelAdmin):
    list_filter = [("date_time", RangeDateFilter)]
