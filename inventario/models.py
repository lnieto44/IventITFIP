# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Tipo_material(models.Model):
    tipo_material = models.CharField('Tipo de material',max_length=80,help_text='Ingrese el tipo de material')

    class Meta:
        db_table = "tipomaterial"

    def __str__(self):
        return self.tipo_material

class Categoria(models.Model):
    descripcion = models.TextField()

    class Meta:
        db_table = "categorias"

    def __str__(self):
        return '{}'.format(self.descripcion)

class Inventario(models.Model):
    descripcion_inventario = models.TextField()
    class Meta:
        db_table = "inventarios"
    def __str__(self):
        return '{}'.format(self.descripcion_inventario)

class TipoActivo(models.Model):
    descripcion = models.TextField()
    t_activos = ((1, "Almacenable"), (2, "Consumible"),)
    tipo_activo = models.SmallIntegerField(choices=t_activos, help_text='Seleccione un tipo de activos')

    class Meta:
        db_table = 'tipos_de_activos'

    def __str__(self):
        return '{}'.format(self.descripcion)

class Activo(models.Model):
    Estados = ((True, "Buen Estado"), (False, "Mal Estado"),)
    nombre_activo = models.CharField('Nombre', db_column='nombre_activo', max_length=60, null=False, blank=False)
    precio_activo = models.DecimalField('Precio', db_column='precio_activo', max_digits=10, decimal_places=2, null=False, blank=False)
    estado_activo = models.BooleanField('Estado',choices=Estados, db_column='estado_activo',default=False, blank=False)
    existencias = models.IntegerField('Existencias', db_column='existencias', null=False, blank=False)
    fecha = models.DateField()
    t_material = models.ForeignKey(Tipo_material)
    tipo_activo = models.ForeignKey(TipoActivo)
    inventario = models.ForeignKey(Inventario)

    class Meta:
        db_table = "activos"

    def __str__(self):
        return '{}'.format(self.nombre_activo)


class Proveedor(models.Model):
    nombre_proveedor = models.CharField('Nombre Proveedor',db_column='nombre_proveedor', max_length=60,help_text='Ingrese el nombre del proveedor')
    direccion_proveedor = models.CharField('Direccion',db_column='direccion_proveedor',  max_length=80,help_text='Ingrese la direccion del proveedor')
    telefono_proveedor = models.CharField('Telefono', db_column='telefono_proveedor', max_length=16, help_text='Ingrese telefono del proveedor')
    email_proveedor = models.EmailField('Email', db_column='email_proveedor', max_length=16, help_text='Ingrese email del proveedor')
    contacto = models.CharField('Contacto', db_column='contacto',  max_length=16, help_text='Ingrese contacto con el proveedor')
    nit = models.CharField('Identificacion', db_column='nit', max_length=12, help_text='Numero Identificacion Proveedor')
    p_fiscal = ((1, "Regimen comun"), (2, "Regimen simplificado"),
                (3, "Gran contribuyente autorretenedor"), (4, "Regimen comun autorretenedor RENTA"),
                (5, "Regimen comun autorretenedor IVA"), (6, "Regimen comun autorretenedor RENTA + IVA"),
                (7, "Regimen especial"), (8, "Gran contribuyente"))
    posicion_fiscal = models.SmallIntegerField(choices=p_fiscal,
                                                   help_text='Seleccione una posicion fiscal')

    class Meta:
        db_table = 'proveedor'

    def __str__(self):
        return '{}'.format(self.nombre_proveedor)

class IngresoActivo(models.Model):
    proveedor = models.OneToOneField(Proveedor)
    fecha_registro = models.DateTimeField()
    doc_origen = models.CharField('Documento origen', max_length=20, help_text='Ingrese documento origen')

    class Meta:
        db_table = 'ingreso_activo'

    def __str__(self):
        return '{}'.format(self.proveedor)


class DetalleIngresoActivo(models.Model):
    ingreso_activo = models.ForeignKey(IngresoActivo)
    activo = models.ForeignKey(Activo)
    cantidad = models.IntegerField('Cantidad', help_text='Ingrese la cantidad')
    precio_activo = models.DecimalField('Precio activos', max_digits=10, decimal_places=2,help_text='Ingrese el precioi del activos')

    class Meta:
        db_table = 'detalle_ingreso_activo'

    def __str__(self):
        return '{}'.format(self.activo)


class Profile(models.Model):
    GENEROS = ((1, "Mujer"),
                   (2, "Hombre"),)

    fecha_nacimiento = models.DateField()
    sexo = models.SmallIntegerField(choices=GENEROS)
    user = models.OneToOneField(User)

    class Meta:
        db_table = "profile"

    def __str__(self):
        return '{}'.format(self.user)


class Municipio(models.Model):
    nombre_municipio = models.CharField(max_length=140)

    class Meta:
        db_table = "municipios"

    def __str__(self):
        return '{}'.format(self.nombre_municipio)

class Sede(models.Model):
    nombre_sede = models.CharField(max_length= 140)
    municipios = models.ForeignKey(Municipio)

    class Meta:
        db_table = "sedes"

    def __str__(self):
        return '{}'.format(self.nombre_sede)

class Facultad(models.Model):
    nombre_facultad = models.CharField(max_length=140)
    sedes = models.ForeignKey(Sede)

    class Meta:
        db_table = "facultades"

    def __str__(self):
        return '{}'.format(self.nombre_facultad)


class Programa(models.Model):
    nombre_programa = models.CharField(max_length=140)

    class Meta:
        db_table = "programas"

    def __str__(self):
        return '{}'.format(self.nombre_programa)


class Dependencia(models.Model):
    nombres_depencia = models.CharField(max_length= 140)
    programas = models.ForeignKey(Programa)

    class Meta:
        db_table = "dependencias"

    def __str__(self):
        return '{}'.format(self.nombres_depencia)

class Cargo(models.Model):
    descripcion = models.TextField()
    jefe_area = models.BooleanField(default=False)
    nombre_cargo = models.CharField(max_length=140)

    class Meta:
        db_table="cargos"

    def __str__(self):
        return '{}'.format(self.nombre_cargo)

class Entrada_Articulos(models.Model):
    ESTADOS_ENTRADA_CHOICES = ((1, "Activo"),
                                   (2, "Inactivo"),
                                   (3, "Dado de baja"),
                                   )
    fecha_entrada_articulo = models.DateTimeField(auto_now=True)
    doc_registro = models.CharField(max_length=140)
    estados_entrada = models.SmallIntegerField(choices=ESTADOS_ENTRADA_CHOICES)

    class Meta:
        db_table="entreda_articulos"

    def __str__(self):
        return '{}'.format(self.doc_registro)

class Detalle_entrada_articulos(models.Model):
    articulo = models.CharField(max_length=140)
    cantidad = models.IntegerField()
    valor_unitario = models.IntegerField()
    sub_total = models.IntegerField()

    class Meta:
        db_table = "detalle_entrada_articulos"

    def __str__(self):
        return '{}'.format(self.articulo)

class Ubicacion(models.Model):
    profile = models.ForeignKey(Profile)
    dependencias = models.ForeignKey(Dependencia)
    activos_ubicaciones = models.ForeignKey(Activo)
    estado_resibir = models.BooleanField()
    estado_entregar = models.BooleanField()
    fecha_recibir = models.DateField()
    fecha_entrega = models.DateField()
    descripcion_recibir = models.CharField(max_length=30)
    descripcion_entrega = models.CharField(max_length=30)

    class Meta:
        db_table = "ubicaciones"

    def __str__(self):
        return '{}'.format(self.profile)

class Recibir(models.Model):
    persona_recibir = models.ForeignKey(Profile)
    dependencia_recibir = models.ForeignKey(Dependencia)

    class Meta:
        db_table = "recibir_cargos"

    def __str__(self):
        return '{}'.format(self.persona_recibir)



