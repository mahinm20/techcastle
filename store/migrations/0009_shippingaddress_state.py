# Generated by Django 3.0.7 on 2020-09-01 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20200901_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='state',
            field=models.CharField(default='', max_length=200),
        ),
    ]
