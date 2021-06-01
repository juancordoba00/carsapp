from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import NullBooleanField
from django.db.models.query import FlatValuesListIterable

# Create your models here.

class Empleados(models.Model):
    cedula_Emp = models.IntegerField(primary_key=True)
    nombre_Emp = models.CharField(max_length=30, blank=False, null=False)
    apellido_Emp = models.CharField(max_length=30, blank=False, null=False)
    cargo_Emp = models.CharField(max_length=30, blank=False, null=False)
    telefono_Emp = models.CharField(max_length=15, blank=False, null=False)
    email_Emp = models.EmailField(blank=False, null=False)

    def __str__(self):
        return f"{self.nombre_Emp} {self.apellido_Emp}"


class Usuario(models.Model):
    ROL = (
        ('Administrador', 'Administrador'),
        ('Recepcionista', 'Recepcionista'),
        ('Empleado', 'Empleado'),
    )
    usuario = models.CharField(max_length=100, unique=True)
    clave = models.CharField(max_length=254)
    rol = models.CharField(max_length=15, choices=ROL, default='3')
    cedula_Emp = models.ForeignKey(Empleados, on_delete=CASCADE, default='0')

    def __str__(self):
        return f"{self.rol}"

class Lista_Cliente(models.Model):
    id_Cliente = models.IntegerField(primary_key=True)
    tipo_Documento = models.CharField(max_length=15, blank=False, null=True)
    tipo_Cliente = models.CharField(max_length=30, blank=False, null=False)
    nombre_Cliente = models.CharField(max_length=30, blank=False, null=False)
    apellido_Cliente = models.CharField(max_length=30, blank=False, null=False)
    email_Cliente = models.EmailField(blank=False, null=False)
    telefono_Cliente = models.CharField(max_length=15, blank=False, null=False)

class EmpleadoXCliente(models.Model):
    id = models.AutoField(primary_key=True)
    id_Empleado_FK = models.ForeignKey(Empleados, on_delete=models.DO_NOTHING)
    id_Cliente_FK = models.ForeignKey(Lista_Cliente, on_delete=models.DO_NOTHING)

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nit = models.CharField(max_length=30, blank=False, null=False)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    direccion = models.CharField(max_length=50, blank=False, null=False)
    telefono = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)    

    def __str__(self):
        return f"{self.nombre}"

class Inventario(models.Model):
    id_Producto = models.AutoField(primary_key=True)
    Ref = models.CharField(max_length=30, blank=False, null=False)
    producto = models.CharField(max_length=30, blank=False, null=False)
    imagen = models.ImageField(upload_to='productos/', null=True)
    provedor = models.ForeignKey(Proveedor, on_delete=models.DO_NOTHING, default='Desconocido')
    stock = models.SmallIntegerField(blank=False, null=False)
    valor_Proveedor = models.IntegerField(blank=False, null=False)
    valor_Venta = models.IntegerField(blank=False, null=False)

class Servicios(models.Model):
    id_Servicio = models.AutoField(primary_key=True)
    tipo_Servicio = models.CharField(max_length=30, blank=False, null=False)
    nombre_Servicio = models.CharField(max_length=30, blank=False, null=False)
    valor_Servicio = models.IntegerField(blank=False, null=False)

class Vehiculo(models.Model):
    id_Vehi = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=7, blank=False, null=False)
    marca = models.CharField(max_length=30, blank=False, null=False)
    modelo = models.CharField(max_length=4, blank=False, null=False)
    color = models.CharField(max_length=30, blank=False, null=False)
    id_Cliente = models.ForeignKey(Lista_Cliente, on_delete=CASCADE, null=True)

class RevisionVehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    estadoProceso = models.CharField(max_length=30, null=True, blank=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=CASCADE)
    empleado = models.ForeignKey(Empleados, on_delete=CASCADE, null=True)

class MantenimientoVehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    estadoProceso = models.CharField(max_length=30, null=True, blank=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=CASCADE)
    empleado = models.ForeignKey(Empleados, on_delete=CASCADE, null=True)    


class Cuenta_Servicio(models.Model):
    id_Cuenta = models.AutoField(primary_key=True)
    id_Producto_FK = models.ForeignKey(Inventario, on_delete=models.DO_NOTHING)
    id_Cliente_FK = models.ForeignKey(Lista_Cliente, on_delete=models.DO_NOTHING)

class VehiXServicio(models.Model):
    id_VehiXServ = models.AutoField(primary_key=True)
    id_Servicio_FK = models.ForeignKey(Servicios, on_delete=models.DO_NOTHING)
    id_ProductoFK = models.ForeignKey(Inventario, on_delete=models.DO_NOTHING)
    id_Cuenta_ServicioFK = models.ForeignKey(Cuenta_Servicio, on_delete=models.DO_NOTHING)

class VehiXCliente(models.Model):
    id_VehiXCliente = models.AutoField(primary_key=True)
    idVehiFK = models.ForeignKey(Vehiculo, on_delete=models.DO_NOTHING)
    idClienteFK = models.ForeignKey(Lista_Cliente, on_delete=models.DO_NOTHING)