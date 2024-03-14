# Generated by Django 5.0 on 2024-03-14 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0003_alter_categoria_id_subcategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
    ]
