from django.contrib import admin
from .models import Category, Product
from mptt.admin import MPTTModelAdmin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class MyJsonWidget(JSONEditorWidget):
    options = {
        'statusBar': 'False',
    }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_category_name', ]

    formfield_overrides = {
        models.JSONField : {'widget': MyJsonWidget(
                options = {
                    'mode': 'tree', 
                    'modes': ['view', 'code', 'tree'],
                    'schema': {
                        'type': 'object',
                        'items': {
                            'type': 'string'
                        },
                    },
                },
            )
        },
    }
    
    class Meta:
        fields = '__all__'

    @admin.display(description='Product Category', ordering='category__name')
    def get_category_name(self, obj):
        return obj.category.name
    
    prepopulated_fields = {"slug": ("name",)}