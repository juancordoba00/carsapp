from django.contrib.messages.api import error
from django.core.checks import messages
from django.db.models import query
from django.db.models.aggregates import Count

from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.db import transaction

from django.forms.models import model_to_dict

from datetime import datetime

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
    paginate_by = 7

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
    paginate_by = 7

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
    paginate_by = 7

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
    paginate_by = 7

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
    paginate_by = 7

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
    paginate_by = 7

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
    paginate_by = 7

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
    paginate_by = 7

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

def AgregarServicioLista(request, id):

    revision = RevisionVehiculo.objects.get(pk = id)
    q = Servicios.objects.all()
    q2 = Vehiculo.objects.get(pk = revision.vehiculo.id_Vehi)
    contexto = {'dato': q}
    
    request.session['vehiRevision'] = [revision.id]
    request.session['vehiculo'] = [q2.id_Vehi, q2.placa]

    return render(request, 'carsapp/agregarServicio.html', contexto)
        
def agregarServicioAVehiculo(request, id):

    revision = request.session['vehiRevision'][0]
    redirect_url = reverse('carsapp:AgregarServicioLista', args=[revision])
    
    if request.method == "GET":
        stage = request.session.get('stage', False)

        vehi = request.session['vehiculo'][0]
        conteo = 0

        encontrado = False
        if not stage:
            request.session['stage'] = [{'servicio': id, 'vehiculo': vehi}]
            encontrado = True
            messages.success(request, 'Servicio agregado correctamente..!')


        else:    
            # Averiguar se existe en variable de session
            for i in request.session['stage']:
                if i["servicio"] == id:
                    print("Encontrado...")
                    encontrado = True
                    messages.success(request, 'El servicio ya se encentra asignado !')
                    break

            if not encontrado:
                # Agregar nuevo servicio
                print("No encontrado... se crea uno nuevo")
                stage.append({ "servicio": id, "vehiculo": vehi })
                conteo += 1
                encontrado = False
                messages.success(request, 'Servicio agregado correctamente..!')


        request.session["encontrado"] = encontrado
        print("Stage acutal: ", request.session["stage"])

        #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return HttpResponseRedirect(redirect_url)

    else:
        return HttpResponseRedirect(reverse('carsapp:RevisionVehiLista', args=() ))

def quitarServicioDeStage(request, id):
    # Recorrer, buscar y eliminar en variable de session
    stage = request.session['stage']
    tamañoStage = len(stage)
    print(tamañoStage)

    count = 0
    if stage:
        for i in stage:

            count += 1
            if i["servicio"] == id:
                print("Encontrado y eliminado")
                stage.remove(i)
                messages.success(request, 'Servicio eliminado correctamente !')
                break

            if count == tamañoStage: 
                print('Este serivcio no se encuentra en zona de stage')
                messages.success(request, 'Este servicio no ha sido asigando al vehículo !')

        request.session["stage"] = stage
        print('Stage actual: ', request.session['stage'])
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
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

        # Recorrer variable de session stage para agregar registros a la DB
        if request.session['stage']:
            for i in request.session['stage']:
                servi = Servicios.objects.get(pk = i['servicio'])
                vehi = Vehiculo.objects.get(pk = i['vehiculo'])
                q2 = VehiXServicio(
                    id_Servicio = servi,
                    id_Vehi = vehi
                )
                q2.save()
            del request.session['stage']
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
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Mantenimiento'

        return context

def mantenimientoEliminar(request, id):
    try:
        q = MantenimientoVehiculo.objects.get(pk = id)
        q2 = VehiXServicio.objects.filter(id_Vehi = q.vehiculo)
        q.delete()
        q2.delete()
        messages.success(request, 'Vehículo eliminado de mantenimiento correctamente..!')
    except IntegrityError:
        messages.error(request, "No puede eliminar este vehículo en revisión porque existen registros.")
    except:
        messages.error(request, "Ocurrió un error")
        
    return HttpResponseRedirect(reverse('carsapp:MantenimientoVehiLista', args=() ))

def mantenimientoDetalles(request, id):
    q = MantenimientoVehiculo.objects.get(pk = id)
    q2 = Vehiculo.objects.get(pk = q.vehiculo.id_Vehi)
    query = VehiXServicio.objects.filter(id_Vehi = q2.id_Vehi)

    contexto = {'datos': query}
    return render(request, 'carsapp/mantenimientoDetalles.html', contexto)
    
def mantenimientoServicioEliminar(request, id):

    mantenimiento = request.session['vehiMantenimiento'][0]
    redirect_url = reverse('carsapp:mantenimientoDetalles', args=[mantenimiento])

    try:
        q = VehiXServicio.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Servicio eliminado correctamente..!')
    except IntegrityError:
        messages.error(request, "No puede eliminar este vehículo en revisión porque existen registros.")
   
    
    return HttpResponseRedirect(redirect_url)

def vaciarSessionServis(request, id):

    del request.session['servis']
    redirect_url = reverse('carsapp:agregarOtroServiList', args=[id])

    return HttpResponseRedirect(redirect_url)


def agregarOtroServiList(request, id):

    q = Servicios.objects.all()

    mantenimiento = MantenimientoVehiculo.objects.get(pk = id)
    request.session['vehiMantenimiento'] = [mantenimiento.vehiculo.id_Vehi]

    query = VehiXServicio.objects.filter(id_Vehi = mantenimiento.vehiculo.id_Vehi)
    print(query)
    if request.method == 'GET':
        servis = request.session.get('servis', False)
        count = 0
        for i in query:
            count += 1
            instancia = model_to_dict(i)
            print(instancia, ' --- ', count)

            encontrado = False
            if not servis:
                print('Servis vacio... Se agrega')
                request.session['servis'] = [{'servicio': instancia['id_Servicio'], 'vehiculo': instancia['id_Vehi']}]
                encontrado = True
            
            if not encontrado:
                print('No encontrado... Se agrega!')
                servis.append({ "servicio": instancia['id_Servicio'], "vehiculo": instancia['id_Vehi']})


    print('Servicios actuales: ', request.session['servis'])
    contexto = {'dato': q}

    return render(request, 'carsapp/agregarOtroServicio.html', contexto)

def agregarOtroServiAVehi(request, id):

    mantenimiento = MantenimientoVehiculo.objects.get(pk = id)
    vehi = Vehiculo.objects.get(pk = mantenimiento.vehiculo)

    revision = request.session['vehiRevision'][0]
    redirect_url = reverse('carsapp:AgregarServicioLista', args=[revision])
    
    if request.method == "GET":
        stage = request.session.get('stage', False)

        vehi = request.session['vehiculo'][0]
        conteo = 0

        encontrado = False
        if not stage:
            request.session['stage'] = [{'servicio': id, 'vehiculo': vehi}]
            encontrado = True
            messages.success(request, 'Servicio agregado correctamente..!')


        else:    
            # Averiguar se existe en variable de session
            for i in request.session['stage']:
                if i["servicio"] == id:
                    print("Encontrado...")
                    encontrado = True
                    messages.success(request, 'El servicio ya se encentra asignado !')
                    break

            if not encontrado:
                # Agregar nuevo servicio
                print("No encontrado... se crea uno nuevo")
                stage.append({ "servicio": id, "vehiculo": vehi })
                conteo += 1
                encontrado = False
                messages.success(request, 'Servicio agregado correctamente..!')


        request.session["encontrado"] = encontrado
        print("Stage acutal: ", request.session["stage"])

        #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return HttpResponseRedirect(redirect_url)

    else:
        return HttpResponseRedirect(reverse('carsapp:RevisionVehiLista', args=() ))

# Facturas

def crearFacturaServicios(request, id):
    try:
        mantenimiento = MantenimientoVehiculo.objects.get(pk = id)
        vehi = Vehiculo.objects.get(pk = mantenimiento.vehiculo.id_Vehi)
        cliente = Lista_Cliente.objects.get(pk = vehi.id_Cliente.id_Cliente)
        query = VehiXServicio.objects.filter(id_Vehi = mantenimiento.vehiculo.id_Vehi)

        fechaPedido = datetime.now() #"2021-05-31 00:00:00"

        total = 0
        for i in query:
            total += i.id_Servicio.valor_Servicio

        q = Facturas(
            totalAPagar = total,
            fecha = fechaPedido,
            id_Cliente = cliente,
            id_Vehi = vehi,
        )
        q.save()
        factu = Facturas.objects.get(pk = q.id)
        for i in query:
            servi = Servicios.objects.get(pk = i.id_Servicio.id_Servicio)
            factura = Facturas.objects.get(pk = factu.id)
            q2 = DetallesFacturas(
                id_Servicio = servi,
                id_Factura = factura,
            )
            q2.save()
        
        query.delete()
        mantenimiento.delete()
        messages.success(request, 'Factura generada correctamente..!')
    except IntegrityError:
        messages.error(request, "No puede crear la factura porque existen registros.")
    #except:
     #   messages.error(request, "Oops... Ocurrio un error")

    return HttpResponseRedirect(reverse('carsapp:MantenimientoVehiLista', args=() ))

class FacturasLista(ListView) :
    template_name = 'carsapp/facturasLista.html'
    queryset = Facturas.objects.all()
    paginate_by = 7

def facturasDetalles(request, id):
    factura = Facturas.objects.get(pk = id)
    query = DetallesFacturas.objects.filter(id_Factura = factura.id)

    contexto = {'datos': query}
    return render(request, 'carsapp/facturasDetalles.html', contexto)


# Carrito 

def vender(request):
    q = Inventario.objects.all().order_by('producto')
    contexto = { "datos" : q }
    return render(request, 'carsapp/vender.html', contexto)

def agregarCarrito(request, id):

    if request.method == "GET":
        
        bolsa = request.session.get('bolsa', False)
        carrito = request.session.get('carrito', False)
        cant = request.GET["cantidad"]
        
        conteo = 0
        if not bolsa:
            request.session["carrito"] = [{ "producto": id, "cantidad": cant }]
            conteo +=1
            request.session["bolsa"] = conteo
            print("no existe", request.session["carrito"], " cantidad: ", request.session["bolsa"])
        else:
            conteo = bolsa
            #averiguar si existe primero en variable de sesion
            encontrado = False
            for r in carrito:
                if r["producto"] == id:
                    print("Encontrado...")
                    #actualizar cantidad
                    r["cantidad"] = int(r["cantidad"]) + int(cant)
                    encontrado = True
                    break
                
            if not encontrado:
                #crear nuevo
                print("No encontrado, se crea nuevo...")
                carrito.append({ "producto": id, "cantidad": cant })
                conteo += 1

            request.session["carrito"] = carrito
            request.session["bolsa"] = conteo

            print("existe agrego: ", request.session["carrito"], " cantidad: ", request.session["bolsa"])
        
        return HttpResponse (conteo)
    else:
        return HttpResponseRedirect(reverse('carsapp:inicio', args=() ))
    

def verCarrito(request):
    #recorrer variable de sesion CARRITO
    carrito = request.session.get('carrito', False)
    clientes = Lista_Cliente.objects.all()
    if carrito:
        total = 0
        for productos in carrito:
            q = Inventario.objects.get(id_Producto = productos["producto"])
            productos['nombre'] = q.producto
            productos["precio"] = q.valor_Venta
            productos["foto"] = q.imagen
            productos["subtotal"] = int(productos["cantidad"]) * q.valor_Venta
            total += productos["subtotal"]

        contexto = { "datos": carrito, "total": total, 'clientes': clientes}
        print('Este es el carrito: ', carrito)
        return render(request, 'carsapp/vender_ver.html', contexto)
    else:
        return HttpResponseRedirect(reverse('carsapp:vender', args=() ))

def quitarProducto(request, id):
    #recorrer, buscar y eliminar producto en variable de sesion CARRITO
    carrito = request.session.get('carrito', False)
    bolsa = request.session.get('bolsa', False)
    
    if carrito:
        for productos in carrito:
            if productos["producto"] == id:
                print("encontrado y eliminado")
                carrito.remove(productos)
                bolsa -= 1

            print("fin")

        request.session["carrito"] = carrito
        request.session["bolsa"] = bolsa
        return HttpResponseRedirect(reverse('carsapp:ver_carrito', args=() ))
    else:
        return HttpResponseRedirect(reverse('carsapp:vender', args=() ))

def limpiarCarrito(request):
    try:
        del request.session["carrito"]
        del request.session["bolsa"]

        return HttpResponseRedirect(reverse('carsapp:vender', args=() ))
    except:
        return HttpResponseRedirect(reverse('carsapp:ver_carrito', args=() ))

def guardarPedido(request):
    logueado = request.session.get('login', False)
    if logueado :
        #recorrer variable de sesion CARRITO para guardar en base de datos
        carrito = request.session.get('carrito', False)
        if carrito:
            # obtener fecha actual
            fechaPedido = datetime.now() #"2021-05-31 00:00:00"
            print(request.POST['cliente'])
            cliente = Lista_Cliente.objects.get(pk = request.POST['cliente'])

            totalPagar = 0
            for i in carrito:
                p = Inventario.objects.get(id_Producto = int(i['producto']))
                totalPagar += p.valor_Venta

            from django.db import transaction
            try:
                with transaction.atomic():

                    #creando encabezado pedido
                    q = Facturas(totalAPagar = totalPagar, fecha = fechaPedido, id_Cliente = cliente)
                    q.save()
                    ultimo = Facturas.objects.latest('id')
                    print("Encabezado Pedido: ", ultimo)

                    
                    for productos in carrito:
                        pro = Inventario.objects.get(id_Producto = int(productos["producto"]))
                        
                        #control stock
                        if int(productos["cantidad"]) <= pro.stock:
                            #guardado masivo
                            print('Holaaaaaaaaa')
                            print('id_prodcuto: ', pro, 'precio: ', pro.valor_Venta, 'cantidad: ', int(productos["cantidad"]), 'id_factura: ', ultimo)
                            DetallesFacturas.objects.create(id_Producto = pro, precio = pro.valor_Venta, cantidad_Producto = int(productos["cantidad"]), id_Factura = ultimo)
                            #disminuir stock producto
                            pro.stock -= int(productos["cantidad"])
                            pro.save()
                        else:
                            messages.error(request, "Cantidad de producto " + str(productos["producto"]) + " supera STOCK " + str(pro.stock))
                            raise Exception("stock")

                    #vaciar carrito
                    del request.session["carrito"]
                    del request.session["bolsa"]
                    messages.success(request, 'Factura generada Correctamente..!')

                    return HttpResponseRedirect(reverse('carsapp:FacturasLista', args=() ))
            except:
                messages.error(request, "Ocurrió un error generando la factura")
                return HttpResponseRedirect(reverse('carsapp:ver_carrito', args=() ))
        else:
            return HttpResponseRedirect(reverse('carsapp:vender', args=() ))
    else:
        messages.error(request, "Para poder facturar el pedido debe loguearse primero!")
        return HttpResponseRedirect(reverse('carsapp:index', args=() ))


def editarCarrito(request, id, cantidad):
    #recorrer, buscar y actualizar cantidad en producto de variable de sesion CARRITO
    carrito = request.session.get('carrito', False)
    
    if carrito:
        for productos in carrito:
            if productos["producto"] == id:
                print("encontrado y actualizado")
                productos["cantidad"] = int(cantidad)

            print("fin")

        request.session["carrito"] = carrito
        return HttpResponse("OK")
    else:
        return HttpResponse("No existe carrito.")