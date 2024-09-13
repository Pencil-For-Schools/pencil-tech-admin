from django.apps import AppConfig
from django.contrib.auth.apps import AuthConfig


class AdminAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin_app'


class CustomAuthConfig(AuthConfig):
    name = 'django.contrib.auth'
    verbose_name = 'User Admin'
