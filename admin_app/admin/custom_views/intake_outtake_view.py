from django.views.generic import TemplateView
from unfold.admin import ModelAdmin
from unfold.views import UnfoldModelAdminViewMixin
from admin_app.views.shopping_views import InventoryIntakeOrAdjustment

class IntakeOuttakeView(TemplateView):
    title = "Inventory Stock Control"
    template_name = "inventory_adjustment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "items": 
            }
        )
        return context

@admin.register(MyModel)
class ExampleCustomView(ModelAdmin):
    def get_urls(self):
        return super().get_urls() + [
            path(
                "custom-url-path",
                MyClassBasedView.as_view(model_admin=self),  # IMPORTANT: model_admin is required
                name="custom_name"
            ),
        ]