from django.views.generic import TemplateView


class IntakeOuttakeView(TemplateView):
    title = "Inventory Stock Control"
    template_name = "inventory_adjustment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "test": "HELLO THERE!!!"
            }
        )
        return context
