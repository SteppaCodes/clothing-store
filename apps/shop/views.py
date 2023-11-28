from django.shortcuts import render
from django.views import View

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
    

class ProductView(View):
    def get(self,request):
        products = Product.objects.all()
        context = {
                "products": products,
            }
        return render(request, 'shop/products.html', context)
    