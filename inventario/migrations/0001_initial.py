# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-08 02:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_activo', models.CharField(db_column='nombre_activo', max_length=60, verbose_name='Nombre')),
                ('precio_activo', models.DecimalField(db_column='precio_activo', decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('estado_activo', models.BooleanField(choices=[(True, 'Buen Estado'), (False, 'Mal Estado')], db_column='estado_activo', default=False, verbose_name='Estado')),
                ('existencias', models.IntegerField(db_column='existencias', verbose_name='Existencias')),
                ('fecha', models.DateField()),
            ],
            options={
                'db_table': 'activos',
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('jefe_area', models.BooleanField(default=False)),
                ('nombre_cargo', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'cargos',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres_depencia', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'dependencias',
            },
        ),
        migrations.CreateModel(
            name='Detalle_entrada_articulos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.CharField(max_length=140)),
                ('cantidad', models.IntegerField()),
                ('valor_unitario', models.IntegerField()),
                ('sub_total', models.IntegerField()),
            ],
            options={
                'db_table': 'detalle_entrada_articulos',
            },
        ),
        migrations.CreateModel(
            name='DetalleIngresoActivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(help_text='Ingrese la cantidad', verbose_name='Cantidad')),
                ('precio_activo', models.DecimalField(decimal_places=2, help_text='Ingrese el precioi del activos', max_digits=10, verbose_name='Precio activos')),
                ('activos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.inventario.Activo')),
            ],
            options={
                'db_table': 'detalle_ingreso_activo',
            },
        ),
        migrations.CreateModel(
            name='Entrada_Articulos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrada_articulo', models.DateTimeField(auto_now=True)),
                ('doc_registro', models.CharField(max_length=140)),
                ('estados_entrada', models.SmallIntegerField(choices=[(1, 'Activo'), (2, 'Inactivo'), (3, 'Dado de baja')])),
            ],
            options={
                'db_table': 'entreda_articulos',
            },
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_facultad', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'facultades',
            },
        ),
        migrations.CreateModel(
            name='IngresoActivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField()),
                ('doc_origen', models.CharField(help_text='Ingrese documento origen', max_length=20, verbose_name='Documento origen')),
            ],
            options={
                'db_table': 'ingreso_activo',
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_inventario', models.TextField()),
            ],
            options={
                'db_table': 'inventarios',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_municipio', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'municipios',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.SmallIntegerField(choices=[(1, 'Mujer'), (2, 'Hombre')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_programa', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'programas',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proveedor', models.CharField(db_column='nombre_proveedor', help_text='Ingrese el nombre del proveedor', max_length=60, verbose_name='Nombre Proveedor')),
                ('direccion_proveedor', models.CharField(db_column='direccion_proveedor', help_text='Ingrese la direccion del proveedor', max_length=80, verbose_name='Direccion')),
                ('telefono_proveedor', models.CharField(db_column='telefono_proveedor', help_text='Ingrese telefono del proveedor', max_length=16, verbose_name='Telefono')),
                ('email_proveedor', models.EmailField(db_column='email_proveedor', help_text='Ingrese email del proveedor', max_length=16, verbose_name='Email')),
                ('contacto', models.CharField(db_column='contacto', help_text='Ingrese contacto con el proveedor', max_length=16, verbose_name='Contacto')),
                ('nit', models.CharField(db_column='nit', help_text='Numero Identificacion Proveedor', max_length=12, verbose_name='Identificacion')),
                ('posicion_fiscal', models.SmallIntegerField(choices=[(1, 'Regimen comun'), (2, 'Regimen simplificado'), (3, 'Gran contribuyente autorretenedor'), (4, 'Regimen comun autorretenedor RENTA'), (5, 'Regimen comun autorretenedor IVA'), (6, 'Regimen comun autorretenedor RENTA + IVA'), (7, 'Regimen especial'), (8, 'Gran contribuyente')], help_text='Seleccione una posicion fiscal')),
            ],
            options={
                'db_table': 'proveedor',
            },
        ),
        migrations.CreateModel(
            name='Recibir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dependencia_recibir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.inventario.Dependencia')),
                ('persona_recibir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.inventario.Profile')),
            ],
            options={
                'db_table': 'recibir_cargos',
            },
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sede', models.CharField(max_length=140)),
                ('municipios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.inventario.Municipio')),
            ],
            options={
                'db_table': 'sedes',
            },
        ),
        migrations.CreateModel(
            name='Tipo_material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_material', models.CharField(help_text='Ingrese el tipo de material', max_length=80, verbose_name='Tipo de material')),
            ],
            options={
                'db_table': 'tipomaterial',
            },
        ),
        migrations.CreateModel(
            name='TipoActivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('tipo_activo', models.SmallIntegerField(choices=[(1, 'Almacenable'), (2, 'Consumible')], help_text='Seleccione un tipo de activos')),
            ],
            options={
                'db_table': 'tipos_de_activos',
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_resibir', models.BooleanField()),
                ('estado_entregar', models.BooleanField()),
                ('fecha_recibir', models.DateField()),
                ('fecha_entrega', models.DateField()),
                ('descripcion_recibir', models.CharField(max_length=30)),
                ('descripcion_entrega', models.CharField(max_length=30)),
                ('activos_ubicaciones', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.inventario.Activo')),
                ('dependencias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.inventario.Dependencia')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.inventario.Profile')),
            ],
            options={
                'db_table': 'ubicaciones',
            },
        ),
        migrations.AddField(
            model_name='ingresoactivo',
            name='proveedor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='apps.inventario.Proveedor'),
        ),
        migrations.AddField(
            model_name='facultad',
            name='sedes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.inventario.Sede'),
        ),
        migrations.AddField(
            model_name='detalleingresoactivo',
            name='ingreso_activo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.inventario.IngresoActivo'),
        ),
        migrations.AddField(
            model_name='dependencia',
            name='programas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.inventario.Programa'),
        ),
        migrations.AddField(
            model_name='activos',
            name='inventario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.inventario.Inventario'),
        ),
        migrations.AddField(
            model_name='activos',
            name='t_material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.inventario.Tipo_material'),
        ),
        migrations.AddField(
            model_name='activos',
            name='tipo_activo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.inventario.TipoActivo'),
        ),
    ]
