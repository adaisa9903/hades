from django.db import models
from django.utils import timezone
from datetime import datetime
from core.erp.choices import gender_choices


# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categoria'
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering = ['id']

class Product (models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Nombre')
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='PVP')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'producto'
        verbose_name='Producto'
        verbose_name_plural='Productos'
        ordering = ['id']

class Client (models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=20, unique=True, verbose_name='Dni')
    birthday = models.DateField(default=timezone.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150,  verbose_name='Dirección')
    sex = models.CharField(max_length=150, choices=gender_choices,  verbose_name='Sexo')


    def __str__(self):
        return self.names

    class Meta:
        db_table = 'cliente'
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
        ordering = ['id']

class Sale (models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=timezone.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Subtotal')
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Iva')
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Total')


    def __str__(self):
        return self.cli.names

    class Meta:
        db_table = 'venta'
        verbose_name='Venta'
        verbose_name_plural='Ventas'
        ordering = ['id']

class DetSale (models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    cant = models.IntegerField(default=0, verbose_name='Cantidad')
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio')
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Subtotal')

    def __str__(self):
        return self.prod.name

    class Meta:
        db_table = 'detventa'
        verbose_name='Detalle de Venta'
        verbose_name_plural='Detalles de Ventas'
        ordering = ['id']

