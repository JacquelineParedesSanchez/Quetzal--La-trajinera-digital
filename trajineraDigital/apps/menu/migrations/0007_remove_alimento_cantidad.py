# Generated by Django 3.0.3 on 2020-06-16 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20200616_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alimento',
            name='cantidad',
        ),
    ]
