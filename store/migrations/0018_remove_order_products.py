# Generated by Django 4.0.5 on 2023-03-25 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_order_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
    ]