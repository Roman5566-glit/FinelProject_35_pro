from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
from .models import Product, Category, Brand


class ProductListView(ListView):
    """List view for products"""
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        """Return filtered and sorted products"""
        queryset = (
            Product.objects
            .filter(is_active=True)
            .select_related('category', 'brand')
            .prefetch_related('images')
        )

        q = self.request.GET.get('q')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')
        sort = self.request.GET.get('sort')

        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) |
                Q(description__icontains=q)
            )
        if category:
            queryset = queryset.filter(category__slug=category)
        if brand:
            queryset = queryset.filter(brand__slug=brand)

        if sort == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort == 'price_desc':
            queryset = queryset.order_by('-price')
        elif sort == 'popular':
            queryset = queryset.order_by('-views')
        elif sort == 'new':
            queryset = queryset.order_by('-created_at')

        return queryset

    def get_context_data(self, **kwargs):
        """Add categories and brands to context"""
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        return context


class ProductDetailView(DetailView):
    """Detail view for product"""
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        """Increase product views"""
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save(update_fields=['views'])
        return obj

    def get_context_data(self, **kwargs):
        """Add reviews and review form to context"""
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.select_related('user')
        context['review_form'] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        """Handle review submission"""
        self.object = self.get_object()

        if not request.user.is_authenticated:
            return redirect('login')

        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = self.object
            review.user = request.user
            if not self.object.reviews.filter(user=request.user).exists():
                review.save()

        return redirect('catalog:product_detail', slug=self.object.slug)
