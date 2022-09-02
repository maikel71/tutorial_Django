from django.contrib import admin
from .models import *

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ['nombre']


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'precio',
                    'descripcion', 'fk_categoria', 'imagen_producto')
    search_fields = ['nombre', 'cantidad']


class AlmacenAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'gerente', 'ciudad',
                    'direccion', 'email', 'telefono')
    search_fields = ['nombre', 'ciudad']


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'nacionalidad',
                    'estado', 'fecha_creacion')
    search_fields = ['nombre', 'apellidos']


# perfil Login
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'usuario', 'telefono',
                    'direccion', 'foto_perfil')
    search_fields = ['cedula', 'usuario']


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Almacen, AlmacenAdmin)
admin.site.register(Proveedor, ProveedorAdmin)

# perfil login
admin.site.register(Perfil, PerfilAdmin)
