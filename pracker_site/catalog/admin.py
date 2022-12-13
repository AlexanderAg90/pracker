from django.contrib import admin
from .models import Category, Product
from mptt.admin import MPTTModelAdmin


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_category_name',]

    @admin.display(description='Product Category', ordering='category__name')
    def get_category_name(self, obj):
        return obj.category.name    
    
    prepopulated_fields = {"slug": ("name",)}