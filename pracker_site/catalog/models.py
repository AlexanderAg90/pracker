from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(max_length=255, unique=True, null=True, db_index=True)
    allowed_attributes = models.JSONField(blank=True, null=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = "category"
        verbose_name_plural = "categories"

    class MPTTMeta:
        order_insertion_by = ['name']

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, unique=True, null=True, db_index=True)
    attributes = models.JSONField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    class Meta:
        ordering = ['name']
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return self.name