from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from.models import Product, Category

class HomeView(View):
    def get(self, request):
        products = Product.objects.all()[:6]
        categories = Category.objects.all()
        context = {
            'products':products,
            "categories": categories,
            "rating_range": range(5)
        }
        return render(request, 'shop/home.html', context)
    

class ProductView(ListView):
    model = Product
    paginate_by = 15
    context_object_name = "products"
    template_name = 'shop/products.html'
    
    