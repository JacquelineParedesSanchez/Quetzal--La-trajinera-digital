# Generated by Django 3.0.3 on 2020-06-06 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0002_auto_20200606_2201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrito',
            old_name='products',
            new_name='alimentos',
        ),
    ]