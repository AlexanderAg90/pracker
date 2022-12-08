from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    allowed_attributes = models.JSONField(blank=True, null=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = "category"
        verbose_name_plural = "categories"

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    attributes = models.JSONField(blank=True, null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return self.name