# Generated by Django 3.1.4 on 2021-06-28 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carsapp', '0018_auto_20210628_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallesfacturas',
            name='id_Factura',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='carsapp.facturas'),
        ),
    ]
