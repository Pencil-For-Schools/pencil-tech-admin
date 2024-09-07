from django.contrib import admin
from admin_app.models import InventoryItem, School, InventoryIntake, ScheduleItem, PencilBoxLocation, PencilBoxLocationInventoryItem, IntakeType
# Register your models here.

class SuperuserOnlyAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

@admin.register(School)
class SchoolAdmin(SuperuserOnlyAdmin):
    pass

@admin.register(InventoryItem)
class InventoryItemAdmin(SuperuserOnlyAdmin):
    pass

@admin.register(InventoryIntake)
class InventoryIntakeAdmin(SuperuserOnlyAdmin):
    pass

@admin.register(ScheduleItem)
class ScheduleItemAdmin(SuperuserOnlyAdmin):
    pass

@admin.register(PencilBoxLocation)
class PencilBoxLocationAdmin(SuperuserOnlyAdmin):
    pass

@admin.register(PencilBoxLocationInventoryItem)
class PencilBoxLocationInventoryItemAdmin(SuperuserOnlyAdmin):
    pass

@admin.register(IntakeType)
class IntakeTypeAdmin(SuperuserOnlyAdmin):
    pass
