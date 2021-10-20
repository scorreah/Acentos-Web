# Generated by Django 3.2.7 on 2021-10-20 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('ISBN', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('sinopsis', models.TextField(blank=True)),
                ('titulo', models.CharField(blank=True, max_length=100)),
                ('editorial', models.CharField(blank=True, max_length=50)),
                ('categoria', models.CharField(blank=True, max_length=50)),
                ('puntuacion', models.FloatField(blank=True, null=True)),
                ('edicion', models.CharField(max_length=20, null=True)),
                ('idioma', models.CharField(blank=True, max_length=20)),
                ('noPaginas', models.IntegerField(default=0)),
                ('precio', models.IntegerField(default=0)),
                ('nuevo', models.BooleanField(default=False)),
                ('preventa', models.BooleanField(default=False)),
                ('portada', models.ImageField(upload_to='libros/pictures')),
                ('presentacion', models.CharField(choices=[('TD', 'Tapa dura'), ('TB', 'Tapa blanda'), ('NN', 'None')], default='NN', max_length=2)),
                ('url_libro', models.CharField(blank=True, max_length=80)),
                ('fecha_publicacion', models.DateField()),
            ],
            options={
                'db_table': 'Libro',
            },
        ),
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(blank=True, max_length=280, null=True)),
                ('puntuacion', models.FloatField(blank=True, null=True)),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('libro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='libros.libro')),
            ],
            options={
                'db_table': 'Resena',
            },
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('biografia', models.TextField(blank=True, null=True)),
                ('fechaNacimiento', models.DateField()),
                ('libros', models.ManyToManyField(to='libros.Libro')),
            ],
            options={
                'db_table': 'Autor',
            },
        ),
    ]
