# Generated by Django 5.0.7 on 2024-07-25 12:32

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_datagoa_delete_djangosession'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hewan', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'aff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ApiDatagoa',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('kode_desa', models.CharField(blank=True, max_length=50, null=True)),
                ('kode_karts', models.CharField(blank=True, max_length=50, null=True)),
                ('nama_objek', models.CharField(blank=True, max_length=50, null=True)),
                ('jenis', models.CharField(blank=True, max_length=20, null=True)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField(blank=True, null=True)),
                ('provinsi', models.CharField(blank=True, max_length=50, null=True)),
                ('kabupaten', models.CharField(blank=True, max_length=50, null=True)),
                ('kecamatan', models.CharField(blank=True, max_length=50, null=True)),
                ('desa', models.CharField(blank=True, max_length=50, null=True)),
                ('dukuh', models.CharField(blank=True, max_length=50, null=True)),
                ('tempat_unik', models.CharField(blank=True, max_length=100, null=True)),
                ('letak', models.CharField(blank=True, max_length=50, null=True)),
                ('akses', models.CharField(blank=True, max_length=50, null=True)),
                ('biota', models.CharField(blank=True, max_length=50, null=True)),
                ('potensi', models.CharField(blank=True, max_length=50, null=True)),
                ('pemanfaatan', models.CharField(blank=True, max_length=50, null=True)),
                ('keterangan', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'API_datagoa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataGoaView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_desa', models.CharField(blank=True, max_length=50, null=True)),
                ('kode_karts', models.CharField(blank=True, max_length=50, null=True)),
                ('nama_objek', models.CharField(blank=True, max_length=50, null=True)),
                ('jenis', models.CharField(blank=True, max_length=20, null=True)),
                ('geom_4326', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('provinsi', models.CharField(blank=True, max_length=50, null=True)),
                ('kabupaten', models.CharField(blank=True, max_length=50, null=True)),
                ('kecamatan', models.CharField(blank=True, max_length=50, null=True)),
                ('desa', models.CharField(blank=True, max_length=50, null=True)),
                ('dukuh', models.CharField(blank=True, max_length=50, null=True)),
                ('tempat_unik', models.CharField(blank=True, max_length=100, null=True)),
                ('letak', models.CharField(blank=True, max_length=50, null=True)),
                ('akses', models.CharField(blank=True, max_length=50, null=True)),
                ('biota', models.CharField(blank=True, max_length=50, null=True)),
                ('potensi', models.CharField(blank=True, max_length=50, null=True)),
                ('pemanfaatan', models.CharField(blank=True, max_length=50, null=True)),
                ('keterangan', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'data_goa_view',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='datagoa',
            options={'managed': False},
        ),
    ]