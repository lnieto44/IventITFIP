# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
#from import_export import resources

# Register your models here.
from pip._vendor.distlib import resources

from inventario import models

admin.site.register(models.Tipo_material)
admin.site.register(models.Categoria)
admin.site.register(models.Inventario)
admin.site.register(models.TipoActivo)
admin.site.register(models.Activo)
admin.site.register(models.Proveedor)
admin.site.register(models.IngresoActivo)
#admin.site.register(models.Detalle_entrada_articulo)
admin.site.register(models.Profile)
admin.site.register(models.Municipio)
admin.site.register(models.Sede)
admin.site.register(models.Facultad)
admin.site.register(models.Programa)
admin.site.register(models.Dependencia)
admin.site.register(models.Cargo)
#admin.site.register(models.Entrada_Articulo)
admin.site.register(models.DetalleIngresoActivo)
admin.site.register(models.Ubicacion)

