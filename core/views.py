from django.views.generic import TemplateView

from catalog.models import Product, Category


class HomeView(TemplateView):
    """Home page"""
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['featured_products'] = (
            Product.objects
            .filter(is_active=True)
            .order_by('-views')[:8]
        )

        context['new_products'] = (
            Product.objects
            .filter(is_active=True)
            .order_by('-created_at')[:4]
        )

        context['categories'] = Category.objects.all()[:4]

        return context