# Generated by Django 5.0.7 on 2024-07-25 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_aff_apidatagoa_datagoaview_alter_datagoa_options'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='datagoa',
            table='data_goa',
        ),
    ]