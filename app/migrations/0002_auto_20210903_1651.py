# Generated by Django 3.2.6 on 2021-09-03 10:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customar',
            new_name='Customer',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='products',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='orderplaced',
            old_name='customar',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='orderplaced',
            old_name='orderd_date',
            new_name='ordered_date',
        ),
    ]
