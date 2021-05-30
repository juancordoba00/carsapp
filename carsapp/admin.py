from django.contrib import admin

# Register your models here.
from .models import *

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'clave', 'rol')

admin.site.register(Usuario, UsuarioAdmin)

class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ('cedula_Emp', 'nombre_Emp', 'apellido_Emp', 'cargo_Emp', 'telefono_Emp', 'email_Emp')
    list_filter = ['nombre_Emp']
    search_fields = ['cedula_Emp', 'nombre_Emp']

admin.site.register(Empleados, EmpleadosAdmin)

class Lista_ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_Cliente', 'tipo_Cliente', 'nombre_Cliente', 'apellido_Cliente', 'email_Cliente', 'telefono_Cliente', )
    list_filter = ['id_Cliente']
    search_fields = ['id_Cliente', 'nombre_Cliente']

admin.site.register(Lista_Cliente, Lista_ClienteAdmin)

class InventarioAdmin(admin.ModelAdmin):
    list_display = ('id_Producto', 'Ref', 'producto', 'imagen', 'provedor', 'stock', 'valor_Proveedor', 'valor_Venta', )
    list_filter = ['id_Producto']
    search_fields = ['id_Producto', 'Ref', 'producto', 'provedor', 'stock']

admin.site.register(Inventario, InventarioAdmin)

class ServiciosAdmin(admin.ModelAdmin):
    list_display = ('id_Servicio', 'tipo_Servicio', 'nombre_Servicio', 'valor_Servicio', )
    list_filter = ['id_Servicio']
    search_fields = ['id_Servicio', 'nombre_Servicio']

admin.site.register(Servicios, ServiciosAdmin)

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('id_Vehi', 'placa', 'marca', 'modelo', 'color', )
    list_filter = ['placa']
    search_fields = ['placa', 'nombre_Servicio']

admin.site.register(Vehiculo, VehiculoAdmin)
