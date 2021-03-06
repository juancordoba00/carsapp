# Generated by Django 3.1.4 on 2021-05-02 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta_Servicio',
            fields=[
                ('id_Cuenta', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('cedula_Emp', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_Emp', models.CharField(max_length=30)),
                ('apellido_Emp', models.CharField(max_length=30)),
                ('cargo_Emp', models.CharField(max_length=30)),
                ('telefono_Emp', models.CharField(max_length=15)),
                ('email_Emp', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id_Producto', models.AutoField(primary_key=True, serialize=False)),
                ('Ref', models.CharField(max_length=30)),
                ('producto', models.CharField(max_length=30)),
                ('provedor', models.CharField(default='Desconocido', max_length=30)),
                ('stock', models.SmallIntegerField()),
                ('valor_Proveedor', models.IntegerField()),
                ('valor_Venta', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Lista_Cliente',
            fields=[
                ('id_Cliente', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo_Cliente', models.CharField(max_length=30)),
                ('nombre_Cliente', models.CharField(max_length=30)),
                ('apellido_Cliente', models.CharField(max_length=30)),
                ('email_Cliente', models.EmailField(max_length=254)),
                ('telefono_Cliente', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id_Servicio', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_Servicio', models.CharField(max_length=30)),
                ('nombre_Servicio', models.CharField(max_length=30)),
                ('valor_Servicio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=100, unique=True)),
                ('clave', models.CharField(max_length=254)),
                ('nombre', models.CharField(max_length=254)),
                ('rol', models.CharField(choices=[('1', 'Administrador'), ('2', 'Recepcionista'), ('3', 'Cliente')], default='3', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id_Vehi', models.AutoField(primary_key=True, serialize=False)),
                ('placa', models.CharField(max_length=7)),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=4)),
                ('color', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='VehiXServicio',
            fields=[
                ('id_VehiXServ', models.AutoField(primary_key=True, serialize=False)),
                ('id_Cuenta_ServicioFK', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='carsapp.cuenta_servicio')),
                ('id_ProductoFK', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='carsapp.inventario')),
                ('id_Servicio_FK', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='carsapp.servicios')),
            ],
        ),
        migrations.CreateModel(
            name='VehiXCliente',
            fields=[
                ('id_VehiXCliente', models.AutoField(primary_key=True, serialize=False)),
                ('idClienteFK', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='carsapp.lista_cliente')),
                ('idVehiFK', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='carsapp.vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='EmpleadoXCliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_Cliente_FK', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='carsapp.lista_cliente')),
                ('id_Empleado_FK', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='carsapp.empleados')),
            ],
        ),
        migrations.CreateModel(
            name='EmpleadosXVehiculo',
            fields=[
                ('id_EmpXVehi', models.AutoField(primary_key=True, serialize=False)),
                ('id_EmpleadoFK', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='carsapp.empleados')),
                ('id_Vehi_FK', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='carsapp.vehiculo')),
            ],
        ),
        migrations.AddField(
            model_name='cuenta_servicio',
            name='id_Cliente_FK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='carsapp.lista_cliente'),
        ),
        migrations.AddField(
            model_name='cuenta_servicio',
            name='id_Producto_FK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='carsapp.inventario'),
        ),
    ]
