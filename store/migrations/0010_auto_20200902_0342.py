# Generated by Django 3.0.7 on 2020-09-01 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_shippingaddress_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='state',
            field=models.CharField(max_length=200),
        ),
    ]