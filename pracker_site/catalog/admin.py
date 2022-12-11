from django.contrib import admin
from .models import Category, Product
from mptt.admin import MPTTModelAdmin

class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)