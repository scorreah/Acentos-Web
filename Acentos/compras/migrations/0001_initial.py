# Generated by Django 3.2.7 on 2021-11-21 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('administradores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo_pago', models.CharField(max_length=25)),
                ('metodo_envio', models.CharField(max_length=25)),
                ('costo_total', models.BigIntegerField()),
                ('fecha_compra', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
            options={
                'db_table': 'Compra',
            },
        ),
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_redaccion', models.DateTimeField(auto_now_add=True)),
                ('fecha_respuesta', models.DateTimeField(blank=True, null=True)),
                ('respondido', models.BooleanField(default=False)),
                ('motivo', models.TextField()),
                ('respuesta', models.TextField()),
                ('administrador_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administradores.administrador')),
                ('compra_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='compras.compra')),
            ],
            options={
                'verbose_name': 'Devolucion',
                'verbose_name_plural': 'Devoluciones',
                'db_table': 'Devolucion',
            },
        ),
    ]
