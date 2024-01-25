# Generated by Django 5.0 on 2024-01-17 17:00

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField()),
            ],
            options={
                'db_table': 'emisor',
            },
        ),
        migrations.CreateModel(
            name='EstadoDisposicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField()),
            ],
            options={
                'db_table': 'estado_disposicion',
            },
        ),
        migrations.CreateModel(
            name='GacetaOficial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_publicacion', models.DateField()),
                ('numero', models.IntegerField()),
                ('edicion', models.CharField()),
            ],
            options={
                'db_table': 'gaceta_oficial',
            },
        ),
        migrations.CreateModel(
            name='TiempoDisposicionEstado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
            ],
            options={
                'db_table': 'tiempo_disposicion_estado',
            },
        ),
        migrations.CreateModel(
            name='TipoDisposicionEmite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField()),
            ],
            options={
                'db_table': 'tipo_disposicon_emite',
            },
        ),
        migrations.CreateModel(
            name='TipoDisposicionFuncion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField()),
            ],
            options={
                'db_table': 'tipo_disposicon_funcion',
            },
        ),
        migrations.CreateModel(
            name='Disposicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('resumen', models.TextField(blank=True, max_length=1000)),
                ('numero', models.IntegerField()),
                ('fecha_emision', models.DateField(default=datetime.date(2024, 1, 17))),
                ('fecha_vigor', models.DateField()),
                ('emisor', models.ManyToManyField(to='disposicion.emisor')),
                ('estado_disposicion', models.ManyToManyField(to='disposicion.estadodisposicion')),
                ('id_gaceta', models.ForeignKey(blank=True, db_column='id_gaceta', null=True, on_delete=django.db.models.deletion.CASCADE, to='disposicion.gacetaoficial')),
                ('id_tipo_disposicion_emite', models.ForeignKey(db_column='id_tipo_disposicion_emite', on_delete=django.db.models.deletion.CASCADE, to='disposicion.tipodisposicionemite')),
                ('tipo_disposicion_funcion', models.ManyToManyField(to='disposicion.tipodisposicionfuncion')),
            ],
            options={
                'db_table': 'disposicion',
            },
        ),
        migrations.CreateModel(
            name='NotaCambio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField()),
                ('id_disposicion', models.ForeignKey(db_column='id_disposicion', on_delete=django.db.models.deletion.CASCADE, to='disposicion.disposicion')),
            ],
            options={
                'db_table': 'nota_cambio',
            },
        ),
        migrations.AddField(
            model_name='estadodisposicion',
            name='id_tiempo',
            field=models.ForeignKey(blank=True, db_column='id_tiempo_disposicion_estado', null=True, on_delete=django.db.models.deletion.CASCADE, to='disposicion.tiempodisposicionestado'),
        ),
    ]
