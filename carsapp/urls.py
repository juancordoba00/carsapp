from django.urls import path
from . import views

app_name = 'carsapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', views.inicio, name='inicio'),
    path('shopping/', views.shopping, name='shopping'),

    path('usuarioCrear/<int:id>/', views.usuarioCrear, name='usuarioCrear'),
    path('usuarioGuardar', views.usuarioGuardar, name='usuarioGuardar'),
    path('usuarioListar/', views.UsuarioLista.as_view(), name='usuarioListar'), 
    path('usuarioEliminar/<int:id>/', views.usuarioEliminar, name='usuarioEliminar'),
    path('usuarioFormActualizar/<int:id>/', views.usuarioFormActualizar, name='usuarioFormActualizar'),
    path('usuarioActualizar', views.usuarioActualizar, name='usuarioActualizar'),

    path('empleadoListar/', views.EmpleadoLista.as_view(), name='empleadoListar'), 
    path('empleadoFormulario/', views.empleadoFormulario, name='empleadoFormulario'),
    path('empleadoGuardar/', views.empleadoGuardar, name='empleadoGuardar'),
    path('empleadoEliminar/<int:id>/', views.empleadoEliminar, name='empleadoEliminar'),
    path('empleadoFormActualizar/<int:id>/', views.empleadoFormActualizar, name='empleadoFormActualizar'),
    path('empleadoActualizar', views.empleadoActualizar, name='empleadoActualizar'),
    
    path('clienteListar/', views.ClienteLista.as_view(), name='clienteListar'), 
    path('clienteFormulario/', views.clienteFormulario, name='clienteFormulario'),
    path('clienteGuardar/', views.clienteGuardar, name='clienteGuardar'),
    path('clienteEliminar/<int:id>/', views.clienteEliminar, name='clienteEliminar'),
    path('clienteFormActualizar/<int:id>/', views.clienteFormActualizar, name='clienteFormActualizar'),
    path('clienteActualizar', views.clienteActualizar, name='clienteActualizar'),

    path('vehiculoListar/', views.VehiculoLista.as_view(), name='vehiculoListar'),
    path('vehiculoFormulario/<int:id>/', views.vehiculoFormulario, name='vehiculoFormulario'),
    path('vehiculoGuardar/', views.vehiculoGuardar, name='vehiculoGuardar'),
    path('vehiculoEliminar/<int:id>/', views.vehiculoEliminar, name='vehiculoEliminar'),
    path('vehiculoFormActualizar/<int:id>/', views.vehiculoFormActualizar, name='vehiculoFormActualizar'),
    path('vehiculoActualizar', views.vehiculoActualizar, name='vehiculoActualizar'),

    path('servicioListar/', views.ServicioLista.as_view(), name='servicioListar'),
    path('servicioFormulario/', views.servicioFormulario, name='servicioFormulario'),
    path('servicioGuardar/', views.servicioGuardar, name='servicioGuardar'),
    path('servicioEliminar/<int:id>/', views.servicioEliminar, name='servicioEliminar'),
    path('servicioFormActualizar/<int:id>/', views.servicioFormActualizar, name='servicioFormActualizar'),
    path('servicioActualizar', views.servicioActualizar, name='servicioActualizar'),

    path('proveedorListar/', views.ProveedorLista.as_view(), name='proveedorListar'), 
    path('proveedorFormulario/', views.proveedorFormulario, name='proveedorFormulario'),
    path('proveedorGuardar/', views.proveedorGuardar, name='proveedorGuardar'),
    path('proveedorEliminar/<int:id>/', views.proveedorEliminar, name='proveedorEliminar'),
    path('proveedorFormActualizar/<int:id>/', views.proveedorFormActualizar, name='proveedorFormActualizar'),
    path('proveedorActualizar', views.proveedorActualizar, name='proveedorActualizar'),

    path('inventarioListar/', views.InventarioLista.as_view(), name='inventarioListar'),
    path('inventarioFormulario/', views.inventarioFormulario, name='inventarioFormulario'),
    path('inventarioGuardar/', views.inventarioGuardar, name='inventarioGuardar'),
    path('inventarioEliminar/<int:id>/', views.inventarioEliminar, name='inventarioEliminar'),
    path('inventarioFormActualizar/<int:id>/', views.inventarioFormActualizar, name='inventarioFormActualizar'),
    path('inventarioActualizar', views.inventarioActualizar, name='inventarioActualizar'),

    path('crearRevision/<int:id>/', views.crearRevision, name='crearRevision'),
    path('RevisionVehiLista/', views.RevisionVehiLista.as_view(), name='RevisionVehiLista'),
    path('revisionEliminar/<int:id>/', views.revisionEliminar, name='revisionEliminar'),
    path('asignarEmpleadoRevision/<int:id>/', views.asignarEmpleadoRevision, name='asignarEmpleadoRevision'),
    path('AgregarServicioLista/<int:id>/', views.AgregarServicioLista, name='AgregarServicioLista'),
    path('agregarServicioAVehiculo/<int:id>/', views.agregarServicioAVehiculo, name='agregarServicioAVehiculo'),
    path('quitarServicioDeStage/<int:id>/', views.quitarServicioDeStage, name='quitarServicioDeStage'),

    path('MantenimientoVehiLista/', views.MantenimientoVehiLista.as_view(), name='MantenimientoVehiLista'),
    path('crearMantenimiento/<int:id>/', views.crearMantenimiento, name='crearMantenimiento'),
    path('mantenimientoEliminar/<int:id>/', views.mantenimientoEliminar, name='mantenimientoEliminar'),
    path('mantenimientoDetalles/<int:id>/', views.mantenimientoDetalles, name='mantenimientoDetalles'),
    path('mantenimientoServicioEliminar/<int:id>/', views.mantenimientoServicioEliminar, name='mantenimientoServicioEliminar'),
    path('agregarOtroServiList/<int:id>/', views.agregarOtroServiList, name='agregarOtroServiList'),
    path('agregarOtroServiAVehi/<int:id>/', views.agregarOtroServiAVehi, name='agregarOtroServiAVehi'),
    path('vaciarSessionServis/<int:id>/', views.vaciarSessionServis, name='vaciarSessionServis'),

    path('FacturasLista/', views.FacturasLista.as_view(), name='FacturasLista'),
    path('crearFacturaServicios/<int:id>/', views.crearFacturaServicios, name='crearFacturaServicios'),
    path('facturasDetalles/<int:id>/', views.facturasDetalles, name='facturasDetalles'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    #rutas carrito
    path('vender/', views.vender, name='vender'),
    path('agregar_carrito/<str:id>/', views.agregarCarrito, name='agregar_carrito'),
    path('ver_carrito/', views.verCarrito, name='ver_carrito'),
    path('quitar_producto/<str:id>/', views.quitarProducto, name='quitar_producto'),
    path('limpiar_carrito/', views.limpiarCarrito, name='limpiar_carrito'),
    path('editar_carrito/<str:id>/<int:cantidad>/', views.editarCarrito, name='editar_carrito'),

    path('guardar_pedido/', views.guardarPedido, name='guardar_pedido'),
]
