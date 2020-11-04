from django.contrib import admin
from .models import VideoJuego
from .models import Plataforma
from .models import Desarrolladora
from .models import Detalle
from .models import Boleta
from .models import Sucursal
#from .models import Usuario
# Register your models here.

class JuegoAdmin(admin.ModelAdmin):
    list_display        =['codigo','nombre','categoria','stock','plataforma','descripcion']

    list_display_links  =['codigo','nombre']
admin.site.register(VideoJuego, JuegoAdmin)

class PlataformaAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre']

    list_display_links =['codigo','nombre']

admin.site.register(Plataforma, PlataformaAdmin)

class DesarrolladoraAdmin(admin.ModelAdmin):
    list_display        =['codigo','nombre']

    list_display_links  =['codigo','nombre']

admin.site.register(Desarrolladora, DesarrolladoraAdmin)

class DetalleAdmin(admin.ModelAdmin):
    list_display        =['codigo','cantidad', 'precio', 'subtotal']

    list_display_links  =['codigo']

admin.site.register(Detalle, DetalleAdmin)

class BoletaAdmin(admin.ModelAdmin):
    list_display        =['idBoleta', 'folio','fecha','monto']

    list_display_links  =['idBoleta']
admin.site.register(Boleta, BoletaAdmin)

class SucursalAdmin(admin.ModelAdmin):
    list_display        =['codigo', 'nombre', 'direccion','telefono', 'encargado']

admin.site.register(Sucursal, SucursalAdmin)

#class UsuarioAdmin(admin.ModelAdmin):
 #   list_display        =['nombreUsuario', 'nombre', 'apellido','correo','password']

#admin.site.register(Usuario, UsuarioAdmin)