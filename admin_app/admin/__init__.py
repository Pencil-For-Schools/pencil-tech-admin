from django.contrib import admin
from django.contrib.auth.models import User, Group

from admin_app.models import (IntakeType, InventoryIntake, InventoryItem,
                              PencilBoxLocation,
                              PencilBoxLocationInventoryItem, ScheduleItem,
                              School)

from .model_admin_views import (IntakeTypeAdmin, InventoryIntakeAdmin, InventoryItemAdmin,
                    PencilBoxLocationAdmin,
                    PencilBoxLocationInventoryItemAdmin, ScheduleItemAdmin,
                    SchoolAdmin, UserAdmin)

admin.site.register(InventoryItem, InventoryItemAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(InventoryIntake, InventoryIntakeAdmin)
admin.site.register(ScheduleItem, ScheduleItemAdmin)
admin.site.register(PencilBoxLocation, PencilBoxLocationAdmin)
admin.site.register(PencilBoxLocationInventoryItem,
                    PencilBoxLocationInventoryItemAdmin)
admin.site.register(IntakeType, IntakeTypeAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
