# Generated by Django 3.0.3 on 2020-06-06 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20200605_1031'),
        ('usuarios', '0001_initial'),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='lista_alimentos',
        ),
        migrations.AddField(
            model_name='alimento',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.Categoria'),
        ),
        migrations.AddField(
            model_name='orden',
            name='rden',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.UserCliente'),
        ),
        migrations.AddField(
            model_name='orden',
            name='repartidor_orden',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Repartidor'),
        ),
    ]