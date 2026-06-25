from django.views.generic import TemplateView

from catalog.models import Product


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['featured_products'] = Product.objects.filter(
            is_active=True
        )[:8]

        return context