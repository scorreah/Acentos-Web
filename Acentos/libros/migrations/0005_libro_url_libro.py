# Generated by Django 3.2.7 on 2021-10-03 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0004_alter_libro_portada'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='url_libro',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]