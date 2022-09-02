from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.forms import CharField
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


def url_producto(self, filename):
    ruta = "static/img/Productos/%s/%s" % (self.nombre, str(filename))
    return ruta


class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    cantidad = models.IntegerField()
    precio = models.DecimalField(decimal_places=2, max_digits=4)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to=url_producto, blank=True)
    fk_categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, default="")

    def imagen_producto(self):
        return mark_safe('<a href="/%s" target="_blank"><img src="/%s" hight="50px" width="50px"></a>' % (self.imagen, self.imagen))

    imagen_producto.allow_tags = True

    def __str__(self):
        return self.nombre


class Almacen(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.EmailField()
    ciudad = models.CharField(max_length=40)
    direccion = models.CharField(max_length=140)
    gerente = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)

    class Meta:
        verbose_name = 'Almacen'
        verbose_name_plural = 'Almacenes'

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombre

# PERFIL LOGIN


def url_perfil(self, filename):
    ruta = "static/img/Perfiles/%s/%s" % (self.usuario, str(filename))
    return ruta


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.IntegerField()
    direccion = models.TextField()
    cedula = models.CharField(max_length=10)
    foto = models.ImageField(upload_to=url_perfil)

    def foto_perfil(self):
        return mark_safe('<a href="/%s" target="_blank"><img src="/%s" hight="50px" width="50px"></a>' % (self.foto, self.foto))

    foto_perfil.allow_tags = True

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.usuario.username
