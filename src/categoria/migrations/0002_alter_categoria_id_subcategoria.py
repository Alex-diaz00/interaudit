# Generated by Django 5.0 on 2024-02-11 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='id_subcategoria',
            field=models.ManyToManyField(null=True, related_name='subcategorias', to='categoria.subcategoria', verbose_name='Subcategorías asociadas'),
        ),
    ]
