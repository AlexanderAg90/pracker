from django.contrib import admin
from .models import *
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_category_name',]
    list_filter=(
        ('category', TreeRelatedFieldListFilter),
    )

    @admin.display(description='Product Category', ordering='category__name')
    def get_category_name(self, obj):
        return obj.category.name 
    
    prepopulated_fields = {"slug": ("name",)}


@admin.register(AttributeGroup)
class AttributeGroupAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']
    ordering = ['group']

    @admin.display(description='Attribute Group', ordering='group__name')
    def get_group_name(self, obj):
        return obj.group.name

    list_filter = ['group__name']


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['product', 'attribute', 'value']