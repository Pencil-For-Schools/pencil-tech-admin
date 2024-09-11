from django.views.generic import TemplateView


class ExampleCustomView(TemplateView):
    title = "Custom Title"
    template_name = "example_custom.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "test": "HELLO THERE!!!"
            }
        )
        return context
