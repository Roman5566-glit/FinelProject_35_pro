from django.db.models import Q
from django.views.generic import ListView, DetailView

from .models import Product, Category, Brand


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        queryset = (
            Product.objects
            .filter(is_active=True)
            .select_related('category', 'brand')
            .prefetch_related('images')
        )

        q = self.request.GET.get('q')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')

        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) |
                Q(description__icontains=q)
            )

        if category:
            queryset = queryset.filter(
                category__slug=category
            )

        if brand:
            queryset = queryset.filter(
                brand__slug=brand
            )

        return queryset
    
        sort = self.request.GET.get('sort')

        if sort == 'price_asc':
            queryset = queryset.order_by('price')

        elif sort == 'price_desc':
            queryset = queryset.order_by('-price')

        elif sort == 'popular':
            queryset = queryset.order_by('-views')

        elif sort == 'new':
            queryset = queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()

        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        obj.views += 1
        obj.save(update_fields=['views'])

        return obj