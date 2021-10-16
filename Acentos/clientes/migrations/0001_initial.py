# Generated by Django 3.2.7 on 2021-10-16 02:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('compras', '0005_auto_20211015_2153'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libros', '0009_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ni', models.CharField(max_length=13, unique=True)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('carrito', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='compras.carrito')),
                ('clientes', models.ManyToManyField(to='libros.Libro')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Cliente',
            },
        ),
    ]