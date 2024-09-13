from unfold.admin import ModelAdmin

from admin_app.admin.configs import SuperuserOnlyAdminConfig


class PencilBoxLocationInventoryItemAdmin(SuperuserOnlyAdminConfig, ModelAdmin):  # noqa: E501
    readonly_fields = ["sold","in_stock","last_audited"]
