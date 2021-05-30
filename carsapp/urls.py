from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

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

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


