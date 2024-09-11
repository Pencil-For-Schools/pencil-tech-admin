from unfold.sites import UnfoldAdminSite

from .admin_site_urls_config import AdminSiteURLsConfig


class AdminSite(AdminSiteURLsConfig, UnfoldAdminSite):
    pass


admin_site = AdminSite()
