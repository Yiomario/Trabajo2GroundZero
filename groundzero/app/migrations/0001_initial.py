# Generated by Django 4.2.2 on 2023-06-30 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('edad', models.IntegerField()),
                ('nombre', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[[0, 'Esculturas'], [1, 'Pinturas'], [2, 'Tejidos'], [3, 'Orfebreria']])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateField()),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('arte', models.IntegerField(choices=[[0, 'Esculturas'], [1, 'Pinturas'], [2, 'Tejidos'], [3, 'Orfebreria']])),
                ('descripcion', models.CharField(max_length=42)),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
            ],
        ),
    ]
