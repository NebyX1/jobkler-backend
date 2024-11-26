# Generated by Django 5.1.2 on 2024-11-24 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profession_location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre de la Ciudad')),
                ('code', models.CharField(max_length=5, unique=True, verbose_name='Código de la Ciudad')),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre del Estado')),
                ('code', models.CharField(max_length=5, unique=True, verbose_name='Código del Estado')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
    ]
