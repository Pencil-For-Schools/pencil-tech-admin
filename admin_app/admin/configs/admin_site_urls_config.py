from admin_app.admin.custom_views import ExampleCustomView
from django.urls import path


class AdminSiteURLsConfig():
    def get_urls(self):
        urls = super().get_urls()
        return [
            path(
                "custom-view/",
                ExampleCustomView.as_view(),
                name='custom-view',
            )
        ] + urls
