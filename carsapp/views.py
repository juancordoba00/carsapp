from django.contrib.messages.api import error
from django.core.checks import messages

from django.shortcuts import render
from django.views.generic import ListView
from django.db import transaction


# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.db import IntegrityError
from django.contrib import messages

from .models import *

"""
def handle_uploaded_file(f):
    from django.conf import settings
    from django.core.files.storage import default_storage
    print("Archivo", f)
    print("Ruta: ",settings.MEDIA_ROOT)
    #save_path = os.path.join(settings.MEDIA_ROOT, 'gep/', f)
    save_path = '{0}/{1}'.format('productos', f)
    print(save_path)
    
    path = default_storage.save(save_path, f)
    if path:
        print("ok")
    else:
        print("error")
    return f

def createProducto(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                nombre = request.POST['nombre']
                estado = True if (request.POST["estado"] == 'true') else False
                precio = request.POST['precio']
                categoria = request.POST['categoria']
                descripcion = request.POST['descripcion']
                f = handle_uploaded_file(request.FILES['file'])
                f = 'media/productos/' + str(f)
                print(f)
                producto = Producto(nombre_prod = nombre, precio = precio ,estado_prod = estado, categoria = Categoria.objects.get(pk = categoria), imge = f, descripcion = descripcion)
                producto.save()
        except IntegrityError:
            print("error")        
        return HttpResponseRedirect(reverse('laNegra:showProducto', args=() ))
    else :
        return HttpResponse("nada")  

"""

def login(request):
    try:
        q = Usuario.objects.get(usuario = request.POST['usuario'], clave = request.POST['clave'])
        q2 = Empleados.objects.get(cedula_Emp = request.POST['usuario'])
        request.session["login"] = [q2.nombre_Emp, q2.apellido_Emp, q.rol, q.usuario, q.id]
        return HttpResponseRedirect(reverse('carsapp:inicio', args=() ))
    except Usuario.DoesNotExist:
        #return HttpResponse("Usuario o Clave no existe...!")
        return HttpResponseRedirect(reverse('carsapp:index', args=() ))
    

def logout(request):
    try:
        del request.session["login"]
        return HttpResponseRedirect(reverse('carsapp:index', args=() ))
    except:
        return HttpResponse("No se pudo cerrar sesión, intente de nuevo...")

def inicio(request):
    return render(request, 'carsapp/inicio.html')

def index(request):
    return render( request, 'carsapp/index.html')

def shopping(request):
    return render( request, "carsapp/shopping.html")



#Servicio
class ServicioLista(ListView):
    template_name = 'carsapp/servicioListar.html'
    queryset = Servicios.objects.all()
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Lista de Empleados'

        print(context)

        return context

def servicioFormulario(request):
    return render(request, "carsapp/servicio_Crear.html")

def servicioGuardar(request):
    if request.method == 'POST':

        q = Servicios(
            tipo_Servicio = request.POST['tipo_Servicio'],
            nombre_Servicio = request.POST['nombre_Servicio'],
            valor_Servicio = request.POST['valor_Servicio'],
        )
    q.save()
    messages.success(request, 'Servicio Creado correctamente..!')
    return HttpResponseRedirect(reverse('carsapp:servicioListar', args=() ))

def servicioEliminar(request, id):
    try:
        q = Servicios.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Servicio eliminado correctamente..!')
    except Servicios.DoesNotExist:
        messages.error(request, "No existe el Servicio " + str(id))
    except IntegrityError:
        messages.error(request, "No puede eliminar este Servicio porque existen registros.")
    except:
        messages.error(request, "Ocurrió un error")
        
    return HttpResponseRedirect(reverse('carsapp:servicioListar', args=() ))

def servicioFormActualizar(request, id):
    q = Servicios.objects.get(pk = id)
    contexto = { "dato": q }
    return render(request, 'carsapp/servicioFormActualizar.html', contexto)

def servicioActualizar(request):
    q = Servicios.objects.get(pk = request.POST['id'])

    q.tipo_Servicio = request.POST['tipo_Servicio']
    q.nombre_Servicio = request.POST['nombre_Servicio']
    q.valor_Servicio = request.POST['valor_Servicio']
    
    q.save()
    messages.success(request, 'Servicio actualizado correctamente..!')
    return HttpResponseRedirect(reverse('carsapp:servicioListar', args=() ))

#Inventario
class InventarioLista(ListView):
    template_name = 'carsapp/inventarioListar.html'
    queryset = Inventario.objects.all()
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Lista de Empleados'

        print(context)

        return context

def inventarioFormulario(request):
    proveedor = Proveedor.objects.all()
    contexto = {'proveedor': proveedor}
    return render(request, "carsapp/inventario_Crear.html", contexto)

def inventarioGuardar(request):
    if request.method == 'POST':
        proveedor = Proveedor.objects.get(pk = request.POST['proveedor'])

        q = Inventario(
            Ref = request.POST['Ref'],
            producto = request.POST['producto'],
            imagen = request.FILES['imagen'],
            provedor = proveedor,
            stock = request.POST['stock'],
            valor_Proveedor = request.POST['valor_Proveedor'],
            valor_Venta = request.POST['valor_Venta'],
        )
    q.save()
    messages.success(request, 'Producto Creado correctamente..!')
    return HttpResponseRedirect(reverse('carsapp:inventarioListar', args=() ))

def inventarioEliminar(request, id):
    try:
        q = Inventario.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Producto eliminado correctamente..!')
    except Servicios.DoesNotExist:
        messages.error(request, "No existe el Producto " + str(id))
    except IntegrityError:
        messages.error(request, "No puede eliminar este Producto porque existen registros.")
    except:
        messages.error(request, "Ocurrió un error")
        
    return HttpResponseRedirect(reverse('carsapp:inventarioListar', args=() ))

def inventarioFormActualizar(request, id):
    proveedor = Proveedor.objects.all()
    q = Inventario.objects.get(pk = id)
    contexto = { "dato": q, 'proveedor': proveedor}
    
    return render(request, 'carsapp/inventarioFormActualizar.html', contexto)

def inventarioActualizar(request):
    q = Inventario.objects.get(pk = request.POST['id'])
    proveedor = Proveedor.objects.get(pk = request.POST['proveedor'])

    try:
        q.Ref = request.POST['Ref']
        q.producto = request.POST['producto']
        q.imagen = request.FILES['imagen']
        q.provedor = proveedor
        q.stock = request.POST['stock']
        q.valor_Proveedor = request.POST['valor_Proveedor']
        q.valor_Venta = request.POST['valor_Venta']

        q.save()
        messages.success(request, 'Producto actualizado correctamente..!')
        return HttpResponseRedirect(reverse('carsapp:inventarioListar', args=() ))
    except proveedor.DoesNotExist:
        messages.error(request, "Seleccione el proveedor ")

#Lista_CLiente
class ClienteLista(ListView):
    template_name = 'carsapp/clienteListar.html'
    queryset = Lista_Cliente.objects.all()
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Lista de Empleados'

        print(context)

        return context

def clienteFormulario(request):
    return render(request, "carsapp/cliente_Crear.html")

def clienteGuardar(request):
    if request.method == 'POST':

        q = Lista_Cliente(
            id_Cliente = request.POST['id_Cliente'],
            tipo_Documento = request.POST['tipo_Documento'],
            tipo_Cliente = request.POST['tipo_Cliente'],
            nombre_Cliente = request.POST['nombre_Cliente'],
            apellido_Cliente = request.POST['apellido_Cliente'],
            email_Cliente = request.POST['email_Cliente'],
            telefono_Cliente = request.POST['telefono_Cliente'],
        )
    q.save()
    messages.success(request, 'Cliente Creado correctamente..!')
    return HttpResponseRedirect(reverse('carsapp:clienteListar', args=() ))

def clienteEliminar(request, id):
    try:
        q = Lista_Cliente.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Cliente eliminado correctamente..!')
    except Servicios.DoesNotExist:
        messages.error(request, "No existe el Cliente " + str(id))
    except IntegrityError:
        messages.error(request, "No puede eliminar este Cliente porque existen registros.")
    except:
        messages.error(request, "Ocurrió un error")
        
    return HttpResponseRedirect(reverse('carsapp:clienteListar', args=() ))

def clienteFormActualizar(request, id):
    q = Lista_Cliente.objects.get(pk = id)
    contexto = { "dato": q }
    return render(request, 'carsapp/clienteFormActualizar.html', contexto)

def clienteActualizar(request):
    q = Lista_Cliente.objects.get(pk = request.POST['id'])

    q.tipo_Documento = request.POST['tipo_Documento']
    q.tipo_Cliente = request.POST['tipo_Cliente']
    q.nombre_Cliente = request.POST['nombre_Cliente']
    q.apellido_Cliente = request.POST['apellido_Cliente']
    q.email_Cliente = request.POST['email_Cliente']
    q.telefono_Cliente = request.POST['telefono_Cliente']
    
    q.save()
    messages.success(request, 'Cliente actualizado correctamente..!')
    return HttpResponseRedirect(reverse('carsapp:clienteListar', args=() ))

#Vehiculo

def vehiculoFormulario(request, id):
    q = Lista_Cliente.objects.get(pk = id)
    contexto = {'dato': q}
    return render(request, "carsapp/vehiculo_Crear.html", contexto)

def vehiculoGuardar(request):
    if request.method == 'POST':
        cliente = Lista_Cliente.objects.get(pk = request.POST['id'])

        q = Vehiculo(
            placa = request.POST['placa'],
            marca = request.POST['marca'],
            modelo = request.POST['modelo'],
            color = request.POST['color'],
            id_Cliente = cliente,
        )
    q.save()
    messages.success(request, 'Vehiculo Creado correctamente..!')
    return HttpResponseRedirect(reverse('carsapp:vehiculoListar', args=() ))

class VehiculoLista(ListView):
    template_name = 'carsapp/vehiculoListar.html'
    queryset = Vehiculo.objects.all()
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente'] = Lista_Cliente.objects.all()

        print(context)

        return context

def vehiculoEliminar(request, id):
    try:
        q = Vehiculo.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Vehiculo eliminado correctamente..!')
    except Vehiculo.DoesNotExist:
        messages.error(request, "No existe el Vehiculo " + str(id))
    except IntegrityError:
        messages.error(request, "No puede eliminar este Vehiculo porque existen registros.")
    except:
        messages.error(request, "Ocurrió un error")
        
    return HttpResponseRedirect(reverse('carsapp:vehiculoListar', args=() ))

def vehiculoFormActualizar(request, id):
    q = Vehiculo.objects.get(pk = id)
    contexto = { "dato": q }
    return render(request, 'carsapp/vehiculoFormActualizar.html', contexto)

def vehiculoActualizar(request):
    q = Vehiculo.objects.get(pk = request.POST['id'])

    q.placa = request.POST['placa']
    q.marca = request.POST['marca']
    q.modelo = request.POST['modelo']
    q.color = request.POST['color']

    q.save()
    messages.success(request, 'Vehiculo actualizado correctamente..!')
    return HttpResponseRedirect(reverse('carsapp:vehiculoListar', args=() ))

#Empleado

class EmpleadoLista(ListView):
    template_name = 'carsapp/empleadoListar.html'
    queryset = Empleados.objects.all()
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Lista de Empleados'

        print(context)

        return context

def empleadoListar(request):
    logueado = request.session.get('login', False)
    if logueado and (logueado[2] == 'Administrador' or logueado[2] == '3'):
        
        q = Empleados.objects.all()
        contexto = { "datos": q }
        return render(request, 'carsapp/empleadoListar.html', contexto)
    else:
        return HttpResponseRedirect(reverse('carsapp:empleadoFormulario', args=() ))

def empleadoFormulario(request):
    return render(request, "carsapp/empleado_Crear.html")

def empleadoGuardar(request):
    if request.method == 'POST':

        q = Empleados(
            cedula_Emp = request.POST['cedula_Emp'],
            nombre_Emp = request.POST['nombre_Emp'],
            apellido_Emp = request.POST['apellido_Emp'],
            cargo_Emp = request.POST['cargo_Emp'],
            telefono_Emp = request.POST['telefono_Emp'],
            email_Emp = request.POST['email_Emp'],
        )
    q.save()
    messages.success(request, 'Empleado Creado correctamente..!')
    return HttpResponseRedirect(reverse('carsapp:empleadoListar', args=() ))

def empleadoEliminar(request, id):
    try:
        q = Empleados.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Empleado eliminado correctamente..!')
    except Servicios.DoesNotExist:
        messages.error(request, "No existe el Empleado " + str(id))
    except IntegrityError:
        messages.error(request, "No puede eliminar este Empleado porque existen registros.")
    except:
        messages.error(request, "Ocurrió un error")
        
    return HttpResponseRedirect(reverse('carsapp:empleadoListar', args=() ))

def empleadoFormActualizar(request, id):
    q = Empleados.objects.get(pk = id)
    contexto = { "dato": q }

    return render(request, 'carsapp/empleadoFormActualizar.html', contexto)

def empleadoActualizar(request):
    q = Empleados.objects.get(pk = request.POST['id'])

    q.nombre_Emp = request.POST['nombre_Emp']
    q.apellido_Emp = request.POST['apellido_Emp']
    q.cargo_Emp = request.POST['cargo_Emp']
    q.telefono_Emp = request.POST['telefono_Emp']
    q.email_Emp = request.POST['email_Emp']
    
    q.save()
    messages.success(request, 'Empleado actualizado correctamente..!')
    return HttpResponseRedirect(reverse('carsapp:empleadoListar', args=() ))

#Usuario

def usuarioCrear(request, id):
    q = Empleados.objects.get(pk = id)
    contexto = {"dato": q}

    return render(request, 'carsapp/usuarioCrear.html', contexto)

def usuarioGuardar(request):
    if request.method == 'POST':
        empleado = Empleados.objects.get(pk = request.POST['id'])
        q = Usuario(
            usuario = request.POST['usuario'],
            clave = request.POST['clave'],
            rol = request.POST['rol'],
            cedula_Emp = empleado,
        )
    q.save()
    messages.success(request, 'Usuario Creado correctamente..!')
    return HttpResponseRedirect(reverse('carsapp:empleadoListar', args=() ))

class UsuarioLista(ListView):
    template_name = 'carsapp/usuarioListar.html'
    queryset = Usuario.objects.all()
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(UsuarioLista, self).get_context_data(**kwargs)
        context['empleado'] = Empleados.objects.all()

        print(context)

        return context

def usuarioEliminar(request, id):
    try:
        q = Usuario.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Usuario eliminado correctamente..!')
    except Servicios.DoesNotExist:
        messages.error(request, "No existe el Usuario " + str(id))
    except IntegrityError:
        messages.error(request, "No puede eliminar este Usuario porque existen registros.")
    except:
        messages.error(request, "Ocurrió un error")
        
    return HttpResponseRedirect(reverse('carsapp:usuarioListar', args=() ))

def usuarioFormActualizar(request, id):
    q = Usuario.objects.get(usuario = id)
    q2 = Empleados.objects.get(pk = id)
    contexto = { "dato": q, "dato2": q2}

    return render(request, 'carsapp/usuarioActualizar.html', contexto)

def usuarioActualizar(request):
    q = Usuario.objects.get(usuario = request.POST['usuario'])
    empleado = Empleados.objects.get(pk = request.POST['usuario'])

    q.clave = request.POST['clave']
    q.rol = request.POST['rol']
    q.cedula_Emp = empleado
    
    q.save()
    messages.success(request, 'Usuario actualizado correctamente..!')
    return HttpResponseRedirect(reverse('carsapp:usuarioListar', args=() ))

#Proveedor
class ProveedorLista(ListView):
    template_name = 'carsapp/proveedorListar.html'
    queryset = Proveedor.objects.all()
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Lista de Proveedores'

        print(context)

        return context

def proveedorFormulario(request):
    return render(request, "carsapp/proveedor_Crear.html")

def proveedorGuardar(request):
    if request.method == 'POST':

        q = Proveedor(
            nit = request.POST['nit'],
            nombre = request.POST['nombre'],
            direccion = request.POST['direccion'],
            telefono = request.POST['telefono'],
            email = request.POST['email'],
        )
    q.save()
    messages.success(request, 'Proveedor Creado correctamente..!')
    return HttpResponseRedirect(reverse('carsapp:proveedorListar', args=() ))

def proveedorEliminar(request, id):
    try:
        q = Proveedor.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Proveedor eliminado correctamente..!')
    except Servicios.DoesNotExist:
        messages.error(request, "No existe el Proveedor " + str(id))
    except IntegrityError:
        messages.error(request, "No puede eliminar este Proveedor porque existen registros.")
    except:
        messages.error(request, "Ocurrió un error")
        
    return HttpResponseRedirect(reverse('carsapp:proveedorListar', args=() ))

def proveedorFormActualizar(request, id):
    q = Proveedor.objects.get(pk = id)
    contexto = { "dato": q }

    return render(request, 'carsapp/proveedorFormActualizar.html', contexto)

def proveedorActualizar(request):
    q = Proveedor.objects.get(pk = request.POST['id'])

    q.nit = request.POST['nit']
    q.nombre = request.POST['nombre']
    q.direccion = request.POST['direccion']
    q.telefono = request.POST['telefono']
    q.email = request.POST['email']
    
    q.save()
    messages.success(request, 'Proveedor actualizado correctamente..!')
    return HttpResponseRedirect(reverse('carsapp:proveedorListar', args=() ))

#Procesos revision

def crearRevision(request, id):
    try:
        vehi = Vehiculo.objects.get(pk = id)

        q = RevisionVehiculo(
            estadoProceso = 'En revisión',
            vehiculo = vehi,
        )
        q.save()
        messages.success(request, 'Vehículo enviado a revisión correctamente..!')
    except Servicios.DoesNotExist:
        messages.error(request, "No existe el vehículo " + str(id))
    except IntegrityError:
        messages.error(request, "No puede enviar este vehículo porque existen registros.")
    except:
        messages.error(request, "Ocurrió un error")
        
    return HttpResponseRedirect(reverse('carsapp:vehiculoListar', args=() ))

class RevisionVehiLista(ListView):
    template_name = 'carsapp/revisionVehiListar.html'
    queryset = RevisionVehiculo.objects.all()
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Lista de revisiones de vehículos'

        return context

def revisionEliminar(request, id):
    try:
        q = RevisionVehiculo.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Vehículo eliminado de revisión correctamente..!')
    except IntegrityError:
        messages.error(request, "No puede eliminar este vehículo en revisión porque existen registros.")
    except:
        messages.error(request, "Ocurrió un error")
        
    return HttpResponseRedirect(reverse('carsapp:RevisionVehiLista', args=() ))

def asignarEmpleadoRevision(request, id):
    q = RevisionVehiculo.objects.get(pk = id)
    empleado = Empleados.objects.get(pk = request.session["login"][3])

    q.empleado = empleado
    
    q.save()
    messages.success(request, 'Empleado asignado correctamente..!')
    return HttpResponseRedirect(reverse('carsapp:RevisionVehiLista', args=() ))


#Procesos mantenimineto

def crearMantenimiento(request, id):
    try:
        mantenimiento = RevisionVehiculo.objects.get(pk = id)
        vehi = Vehiculo.objects.get(pk = mantenimiento.vehiculo.id_Vehi)
        emp = Empleados.objects.get(pk = mantenimiento.empleado.cedula_Emp)


        q = MantenimientoVehiculo(
            estadoProceso = 'En mantenimiento',
            vehiculo = vehi,
            empleado = emp,
        )
        q.save()
        mantenimiento.delete()
        messages.success(request, 'Vehículo enviado a mantenimiento correctamente..!')
    except Servicios.DoesNotExist:
        messages.error(request, "No existe el vehículo " + str(id))
    except IntegrityError:
        messages.error(request, "No puede enviar este vehículo porque existen registros.")
    except:
        messages.error(request, "Por favor asigne empleado antes de enviar a mantenimiento !")
        
    return HttpResponseRedirect(reverse('carsapp:RevisionVehiLista', args=() ))

class MantenimientoVehiLista(ListView):
    template_name = 'carsapp/mantenimientoVehiListar.html'
    queryset = MantenimientoVehiculo.objects.all()
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Mantenimiento'

        return context

def mantenimientoEliminar(request, id):
    try:
        q = MantenimientoVehiculo.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Vehículo eliminado de mantenimiento correctamente..!')
    except IntegrityError:
        messages.error(request, "No puede eliminar este vehículo en revisión porque existen registros.")
    except:
        messages.error(request, "Ocurrió un error")
        
    return HttpResponseRedirect(reverse('carsapp:MantenimientoVehiLista', args=() ))
