from django.urls import path
from admin_app.admin import admin_site
from admin_app.views import cancel_checkout, inventory_items

urlpatterns = [
    path('admin/', admin_site.urls),
    path('shopping/cancel/<int:teacher_schedule_item_id>', cancel_checkout),
    path('shopping/inventory_items/<int:location_id>', inventory_items),
]
