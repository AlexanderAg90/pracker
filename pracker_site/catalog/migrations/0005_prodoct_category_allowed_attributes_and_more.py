# Generated by Django 4.1.3 on 2022-12-08 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_rename_category_parent_category_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prodoct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('attributes', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='allowed_attributes',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
