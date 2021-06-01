# Generated by Django 3.2.3 on 2021-05-31 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carsapp', '0014_auto_20210530_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='MantenimientoVehiculo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estadoProceso', models.CharField(blank=True, max_length=30, null=True)),
                ('empleado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carsapp.empleados')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carsapp.vehiculo')),
            ],
        ),
        migrations.DeleteModel(
            name='EmpleadosXVehiculo',
        ),
    ]