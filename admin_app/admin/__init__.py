from django.contrib.auth.models import User

from admin_app.models import (County, IntakeType, InventoryIntake,
                              InventoryItem, Order, PencilBoxLocation,
                              PencilBoxLocationInventoryItem, ScheduleItem,
                              School, Teacher, TeacherScheduleItem)

from .configs import admin_site
from .model_admin_views import (IntakeTypeAdmin, InventoryIntakeAdmin,
                                InventoryItemAdmin, PencilBoxLocationAdmin,
                                PencilBoxLocationInventoryItemAdmin,
                                ScheduleItemAdmin, SchoolAdmin, UserAdmin,
                                TeacherAdmin, CountyAdmin,
                                TeacherScheduleItemAdmin, OrderAdmin)

admin_site.register(InventoryItem, InventoryItemAdmin)
admin_site.register(School, SchoolAdmin)
admin_site.register(InventoryIntake, InventoryIntakeAdmin)
admin_site.register(ScheduleItem, ScheduleItemAdmin)
admin_site.register(PencilBoxLocation, PencilBoxLocationAdmin)
admin_site.register(PencilBoxLocationInventoryItem,
                    PencilBoxLocationInventoryItemAdmin)
admin_site.register(IntakeType, IntakeTypeAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Teacher, TeacherAdmin)
admin_site.register(County, CountyAdmin)
admin_site.register(TeacherScheduleItem, TeacherScheduleItemAdmin)
admin_site.register(Order, OrderAdmin)
