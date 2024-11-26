# Generated by Django 5.1.2 on 2024-11-17 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre del Departamento')),
                ('code', models.CharField(blank=True, max_length=3, null=True, unique=True, verbose_name='Código del Departamento')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre de la Profesión')),
                ('code', models.CharField(blank=True, max_length=3, null=True, unique=True, verbose_name='Código de la Profesión')),
            ],
            options={
                'verbose_name': 'Profesión',
                'verbose_name_plural': 'Profesiones',
            },
        ),
    ]
