# Generated by Django 3.1.4 on 2021-07-05 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carsapp', '0021_facturas_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturas',
            name='id_Vehi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='carsapp.vehiculo'),
        ),
        migrations.AlterField(
            model_name='facturas',
            name='totalAPagar',
            field=models.IntegerField(null=True),
        ),
    ]
