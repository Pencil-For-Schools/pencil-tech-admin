from django.contrib import admin
from admin_app.models import InventoryItem, School, InventoryIntake, ScheduleItem, PencilBoxLocation, PencilBoxLocationInventoryItem, IntakeType
# Register your models here.

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    pass

@admin.register(InventoryIntake)
class InventoryIntakeAdmin(admin.ModelAdmin):
    pass

@admin.register(ScheduleItem)
class ScheduleItemAdmin(admin.ModelAdmin):
    pass

@admin.register(PencilBoxLocation)
class PencilBoxLocationAdmin(admin.ModelAdmin):
    pass

@admin.register(PencilBoxLocationInventoryItem)
class PencilBoxLocationInventoryItemAdmin(admin.ModelAdmin):
    pass

@admin.register(IntakeType)
class IntakeTypeAdmin(admin.ModelAdmin):
    pass
