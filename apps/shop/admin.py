from django.contrib import admin

from . models import Product, Category, Review

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    list_filter = list_display

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'in_stock', 'created_at', 'updated_at')
    list_filter = list_display

class ReviewAdmin(admin.ModelAdmin):
    list_display=('user', 'product', 'rating', 'created_at', 'updated_at')
    list_filter = list_display

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)