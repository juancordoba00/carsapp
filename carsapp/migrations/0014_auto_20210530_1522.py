# Generated by Django 3.1.4 on 2021-05-30 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carsapp', '0013_auto_20210530_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revisionvehiculo',
            name='empleado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carsapp.empleados'),
        ),
    ]
