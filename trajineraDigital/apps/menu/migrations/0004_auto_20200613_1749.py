# Generated by Django 3.0.3 on 2020-06-13 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20200610_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimento',
            name='foto',
            field=models.ImageField(upload_to='alimentos/images/'),
        ),
    ]
