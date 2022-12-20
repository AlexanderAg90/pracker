from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

class AttributeGroup(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        ordering = ['name']
        verbose_name = "attribute group"
        verbose_name_plural = "attribute groups"

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    group = models.ForeignKey(AttributeGroup, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name = "attribute"
        verbose_name_plural = "attributes"

    def __str__(self):
        return self.name


class Category(MPTTModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(max_length=255, unique=True, null=True, db_index=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    attribute_group = models.OneToOneField(AttributeGroup, null=True, blank=True, on_delete=models.DO_NOTHING)

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    class Meta:
        ordering = ['name']
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return self.name


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='attribute')
    value = models.CharField(max_length=100)