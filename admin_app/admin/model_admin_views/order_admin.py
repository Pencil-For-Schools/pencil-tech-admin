from unfold.admin import ModelAdmin
from django.contrib import admin
from admin_app.admin.configs import SuperuserOnlyAdminConfig


@admin.action(description="approve selected orders")
def approve_orders(modeladmin, request, queryset):
    queryset.update(approved=True)

class OrderAdmin(SuperuserOnlyAdminConfig, ModelAdmin):
    list_display = ["teacher", "approved"]
    actions = [approve_orders]
