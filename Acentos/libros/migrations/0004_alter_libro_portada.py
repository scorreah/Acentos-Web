# Generated by Django 3.2.7 on 2021-10-03 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0003_alter_libro_puntuacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='portada',
            field=models.ImageField(upload_to='libros/pictures'),
        ),
    ]
