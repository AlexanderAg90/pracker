# Generated by Django 4.1.3 on 2022-12-11 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_category_slug_product_slug_alter_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
    ]
