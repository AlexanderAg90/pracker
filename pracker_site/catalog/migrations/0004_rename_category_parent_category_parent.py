# Generated by Django 4.1.3 on 2022-12-07 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_category_options_category_category_parent_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_parent',
            new_name='parent',
        ),
    ]
