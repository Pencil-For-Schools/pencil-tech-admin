"""
URL configuration for inventory_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from admin_app.admin import admin_site
from shopping_api import shopping_url_patterns
from scheduling_api import scheduling_url_patterns
from admin_app.views import cancel_checkout, inventory_items

urlpatterns = [
    path('admin/', admin_site.urls),
    path('shopping/cancel/<int:teacher_schedule_item_id>', cancel_checkout),
    path('shopping/inventory_items/<int:location_id>', inventory_items)
] + shopping_url_patterns + scheduling_url_patterns
