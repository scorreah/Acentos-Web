# Generated by Django 3.2.7 on 2021-11-21 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administradores', '0002_administrador_user'),
        ('clientes', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='administrador_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administradores.administrador'),
        ),
    ]
