# Generated by Django 4.2.4 on 2023-09-04 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idProducto', models.IntegerField(max_length=15)),
                ('idCliente', models.IntegerField(max_length=13)),
                ('direccion', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=10)),
                ('cantidad', models.IntegerField(max_length=10)),
                ('reutilizable', models.CharField(max_length=10)),
                ('bodega', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripccion', models.CharField(max_length=200)),
                ('Proyecto', models.CharField(max_length=20)),
                ('idCliente', models.IntegerField(max_length=13)),
                ('cotizacion', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=30)),
                ('Usuario', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('telefono', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='encargado',
            name='correo',
        ),
    ]