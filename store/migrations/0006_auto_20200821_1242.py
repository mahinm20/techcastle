# Generated by Django 3.0.7 on 2020-08-21 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200814_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product_a',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product_l',
        ),
    ]
