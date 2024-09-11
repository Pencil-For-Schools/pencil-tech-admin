from django.contrib.auth.models import Group, User

from admin_app.models import (IntakeType, InventoryIntake, InventoryItem,
                              PencilBoxLocation,
                              PencilBoxLocationInventoryItem, ScheduleItem,
                              School)

from .configs import admin_site
from .model_admin_views import (IntakeTypeAdmin, InventoryIntakeAdmin,
                                InventoryItemAdmin, PencilBoxLocationAdmin,
                                PencilBoxLocationInventoryItemAdmin,
                                ScheduleItemAdmin, SchoolAdmin, UserAdmin)

admin_site.register(InventoryItem, InventoryItemAdmin)
admin_site.register(School, SchoolAdmin)
admin_site.register(InventoryIntake, InventoryIntakeAdmin)
admin_site.register(ScheduleItem, ScheduleItemAdmin)
admin_site.register(PencilBoxLocation, PencilBoxLocationAdmin)
admin_site.register(PencilBoxLocationInventoryItem,
                    PencilBoxLocationInventoryItemAdmin)
admin_site.register(IntakeType, IntakeTypeAdmin)
admin_site.register(User, UserAdmin)
