# Generated by Django 4.1 on 2025-05-28 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_remove_orderproduct_variations'),
        ('carts', '0007_remove_cartitem_variations'),
        ('store', '0010_alter_productgallery_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.AddField(
            model_name='product',
            name='specifications',
            field=models.TextField(blank=True, verbose_name='Характеристики'),
        ),
        migrations.DeleteModel(
            name='Variation',
        ),
    ]
