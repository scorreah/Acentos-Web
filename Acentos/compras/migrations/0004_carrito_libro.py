# Generated by Django 3.2.7 on 2021-10-15 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0008_auto_20211014_2218'),
        ('compras', '0003_librocarrito'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='libro',
            field=models.ManyToManyField(through='compras.LibroCarrito', to='libros.Libro'),
        ),
    ]
