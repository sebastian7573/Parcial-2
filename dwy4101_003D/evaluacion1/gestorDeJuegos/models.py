from django.db import models

# Create your models here.

class Desarrolladora(models.Model):
    codigo = models.DecimalField(max_digits=13, decimal_places=0)
    nombre = models.TextField(max_length=100)

    def __str__(self):
        return self.nombre

class Plataforma(models.Model):
    codigo = models.DecimalField(max_digits=13, decimal_places=0)
    nombre = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre


class VideoJuego(models.Model):
    desarrolladora = models.ForeignKey(Desarrolladora, blank=True, null=True, on_delete=models.SET_NULL )
    plataforma = models.ForeignKey(Plataforma, blank=True, null=True, on_delete=models.SET_NULL)
    codigo      = models.DecimalField(max_digits=13, decimal_places=0)
    nombre      = models.TextField(max_length=100)
    categoria   = models.TextField(max_length=20)
    descripcion = models.TextField(max_length=1000)
    precioCosto = models.DecimalField(max_digits=20, decimal_places=0)
    precioVenta = models.DecimalField(max_digits=20, decimal_places=0)
    stock       = models.IntegerField()

    def __str__(self):
        return self.nombre


class Sucursal(models.Model):
    codigo = models.DecimalField(max_digits=13, decimal_places=0)
    nombre = models.TextField(max_length=100)
    direccion = models.TextField(max_length=100)
    telefono = models.IntegerField()
    encargado = models.TextField()

    def __str__(self):
        return self.nombre


class Boleta(models.Model):
    sucursal = models.ForeignKey(Sucursal, blank=True, null=True, on_delete=models.SET_NULL)
    idBoleta = models.IntegerField()
    folio = models.IntegerField()
    fecha = models.DateField()
    monto = models.IntegerField()

    def __int__(self):
        return self.idBoleta


class Detalle(models.Model):
    boleta   = models.ForeignKey(Boleta, blank=True, null=True, on_delete=models.SET_NULL )
    videoJuego = models.ForeignKey(VideoJuego, blank=True, null=True, on_delete=models.SET_NULL)    
    codigo = models.DecimalField(max_digits=13, decimal_places=0)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    subtotal = models.IntegerField()

    def __int__(self):
        return self.precio

