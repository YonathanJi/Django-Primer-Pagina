from django.contrib import admin

from gestionPedidos.models import Clientes, Articulos, Pedidos # ahy que importar el modulo

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","tlfn") # Esto es para que muestre las columnas en el panelAdmin
    search_fields=("nombre","tlfn")  #Esto es una bara de busqueda en clientes paneladmin


class ArticulosAdmin(admin.ModelAdmin):
    list_display=("nombre","seccion","precio")
    list_filter=("seccion",) #Esto es un filtro de busqueda en articulos paneladmin


class PedidoAdmin(admin.ModelAdmin):
    list_display=("numero","fecha","entregado")
    list_filter=("fecha",)   #Esto es un filtro de busqueda en articulos paneladmin
    date_hierarchy="fecha" #filtro mijas de pan arriba de las columnas


      

admin.site.register(Clientes,ClientesAdmin) #Registrar el modelo clientes en el panel de administracion
admin.site.register(Articulos,ArticulosAdmin)#Registrar el modelo Articulo en el panel de administracion
admin.site.register(Pedidos,PedidoAdmin)#Registrar el modelo Pedido en el panel de administracion