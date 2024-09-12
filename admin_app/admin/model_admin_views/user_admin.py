from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from unfold.admin import ModelAdmin


class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass
