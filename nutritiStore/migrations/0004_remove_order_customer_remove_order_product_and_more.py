# Generated by Django 4.2.7 on 2023-11-16 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutritiStore', '0003_product_is_sale_product_sale_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
