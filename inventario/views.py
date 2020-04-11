# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Nos devuelve un objeto resultado
from django.http.response import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect, get_object_or_404
from django.urls.base import reverse

# Vista genérica para mostrar resultados
from django.views.generic.base import TemplateView
# Workbook nos permite crear libros en excel

from django.conf import settings
from io import BytesIO
from django.template.loader import get_template
from django.template import Context
import xhtml2pdf.pisa as pisa
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

from reportlab.platypus import (Table, TableStyle)
from reportlab.lib import colors

from django.views.generic import View, DeleteView

from .forms import ProfileForm,UserForm,ActivoForm,CargoForm, LoginForm
from .models import Profile,Cargo,Activo

from django.contrib import messages

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.
@login_required(login_url='login')
def index_cargo(request):
	cargo = Cargo.objects.all()
	return render(request, 'cargos/index.html', {'cargo': cargo})


@login_required(login_url='login')
def view_cargo(request, id_cargo):
	cargo = Cargo.objects.get(id=id_cargo)
	return render(request, 'cargos/view.html', {'cargo': cargo})


@permission_required('django.auth.index_user', login_url='base/login.html')
def create_cargo(request):
	if request.method == 'POST':
		form = CargoForm(request.POST)

		if form.is_valid():
			form.save()

			success = 'Se ha Creado Exitosamente los cargos'
			messages.success(request, success)
			return redirect('cargo:index_cargo')
		else:
			success = "No Se ha Creado Exitosamente los cargos"
			messages.error(request, success)
			return redirect('cargo:create_cargo')

	else:
		form = CargoForm()

	return render(request, 'cargos/form.html', {'form': form})


@permission_required('django.auth.index_user', login_url='base/login.html')
def edit_cargo(request, id_cargo):
	cargo = Cargo.objects.get(id=id_cargo)
	if request.method == 'GET':
		cargo = CargoForm(instance=cargo)
	else:
		cargo = CargoForm(request.POST, instance=cargo)
		if cargo.is_valid():
			cargo.save()
		succeess = 'Ha actualizado exitosamanente los cargos'
		messages.success(request, succeess)
		return HttpResponseRedirect(reverse("cargo:index_cargo"))

	return render(request, 'cargos/edit.html', {'form': cargo})


@permission_required('django.auth.index_user', login_url='base/login.html')
def delete_cargo(request, id_cargo):
	"""
	try:
		form = Cargo.objects.get(id=id_cargo)
	except Cargo.DoesNotExist:
		raise Http404
	"""
	form = get_object_or_404(Cargo, id=id_cargo)

	if request.method == 'POST':
		form.delete()
		return redirect('cargo:index_cargo')

	return render(request, 'cargos/delete.html', {'form': form})


@login_required(login_url='login')
def index_activo(request):
	activo = Activo.objects.all()
	return render(request, 'activos/index.html', {'activo': activo})


@login_required(login_url='login')
def create_activo(request):
	if request.method == 'POST':
		form = ActivoForm(request.POST)

		if form.is_valid():
			form.save()

			success = 'Se ha Creado Exitosamente los activos'
			messages.success(request, success)
			return redirect('activo:index_activo')
		else:
			success = "No Se ha Creado Exitosamente los activos"
			messages.error(request, success)
			return redirect('activo:create_activo')

	else:
		form = ActivoForm()

	return render(request, 'activos/form.html', {'form': form})



@permission_required('django.auth.index_user', login_url='base/login.html')
def edit_activo(request, id_activo):
	activo = Activo.objects.get(id=id_activo)
	if request.method == 'GET':
		activo = ActivoForm(instance=activo)
	else:
		activo = ActivoForm(request.POST, instance=activo)
		if activo.is_valid():
			activo.save()
		succeess = 'Ha actualizado exitosamanente los activos'
		messages.success(request, succeess)
		return HttpResponseRedirect(reverse("activo:index_activo"))

	return render(request, 'activos/edit.html', {'form': activo})


@permission_required('django.auth.index_user', login_url='base/login.html')
def delete_activo(request, id_activo):
	"""
	try:
		form = activos.objects.get(id=id_activo)
	except activos.DoesNotExist:
		raise Http404
	"""
	form = get_object_or_404(Activo, id=id_activo)

	if request.method == 'POST':
		form.delete()
		return redirect('activo:index_activo')

	return render(request, 'activos/delete.html', {'form': form})


@login_required(login_url='login')
def view_activo(request, id_activo):
	activo = Activo.objects.get(id=id_activo)
	return render(request, 'activos/view.html', {'activo': activo})



@login_required(login_url='login')
def view_cargo(request, id_cargo):
	cargo = Cargo.objects.get(id=id_cargo)
	return render(request, 'cargos/view.html', {'cargo': cargo})


@permission_required('django.auth.index_user', login_url='base/login.html')
def create_cargo(request):
	if request.method == 'POST':
		form = CargoForm(request.POST)

		if form.is_valid():
			form.save()

			success = 'Se ha Creado Exitosamente los cargos'
			messages.success(request, success)
			return redirect('cargo:index_cargo')
		else:
			success = "No Se ha Creado Exitosamente los cargos"
			messages.error(request, success)
			return redirect('cargo:create_cargo')

	else:
		form = CargoForm()

	return render(request, 'cargos/form.html', {'form': form})


@permission_required('django.auth.index_user', login_url='base/login.html')
def edit_cargo(request, id_cargo):
	cargo = Cargo.objects.get(id=id_cargo)
	if request.method == 'GET':
		cargo = CargoForm(instance=cargo)
	else:
		cargo = CargoForm(request.POST, instance=cargo)
		if cargo.is_valid():
			cargo.save()
		succeess = 'Ha actualizado exitosamanente los cargos'
		messages.success(request, succeess)
		return HttpResponseRedirect(reverse("cargo:index_cargo"))

	return render(request, 'cargos/edit.html', {'form': cargo})


@permission_required('django.auth.index_user', login_url='base/login.html')
def delete_cargo(request, id_cargo):
	"""
	try:
		form = Cargo.objects.get(id=id_cargo)
	except Cargo.DoesNotExist:
		raise Http404
	"""
	form = get_object_or_404(Cargo, id=id_cargo)

	if request.method == 'POST':
		form.delete()
		return redirect('cargo:index_cargo')

	return render(request, 'cargos/delete.html', {'form': form})

class CargoDelete(DeleteView):
	model = Cargo
	form_class = ActivoForm
	template_name = "cargos/delete.html"

	def get_context_data(self, **kmargs):
		context_data = super(CargoDelete, self).get_context_data(**kmargs)
		pk = self.kmargs.get('pk')
		cargo = Activo.objects.get(id(pk))
		context_data.update({'cargo': cargo})
		return context_data
	def get_success_url(self):
		return reverse('cargo:index_cargo')


@login_required(login_url='login')
def index_activo(request):
	activo = Activo.objects.all()
	return render(request, 'activos/index.html', {'activo': activo})


@login_required(login_url='login')
def create_activo(request):
	if request.method == 'POST':
		form = ActivoForm(request.POST)

		if form.is_valid():
			form.save()

			success = 'Se ha Creado Exitosamente los activos'
			messages.success(request, success)
			return redirect('activo:index_activo')
		else:
			success = "No Se ha Creado Exitosamente los activos"
			messages.error(request, success)
			return redirect('activo:create_activo')

	else:
		form = ActivoForm()

	return render(request, 'activos/form.html', {'form': form})



@permission_required('django.auth.index_user', login_url='base/login.html')
def edit_activo(request, id_activo):
	activo = Activo.objects.get(id=id_activo)
	if request.method == 'GET':
		activo = ActivoForm(instance=activo)
	else:
		activo = ActivoForm(request.POST, instance=activo)
		if activo.is_valid():
			activo.save()
		succeess = 'Ha actualizado exitosamanente los activos'
		messages.success(request, succeess)
		return HttpResponseRedirect(reverse("activo:index_activo"))

	return render(request, 'activos/edit.html', {'form': activo})

class ActivosDelete(DeleteView):
	model = Activo
	form_class = ActivoForm
	template_name = "activos/delete.html"

	def get_context_data(self, **kmargs):
		context_data = super(ActivosDelete, self).get_context_data(**kmargs)
		pk = self.kmargs.get('pk')
		activo = Activo.objects.get(id(pk))
		context_data.update({'activo': activo})
		return context_data
	def get_success_url(self):
		return reverse('activo:index_activo')


@permission_required('django.auth.index_user', login_url='base/login.html')
def delete_activo(request, id_activo):
	"""
	try:
		form = activos.objects.get(id=id_activo)
	except activos.DoesNotExist:
		raise Http404
	"""
	form = get_object_or_404(Activo, id=id_activo)

	if request.method == 'POST':
		form.delete()
		return redirect('activo:index_activo')

	return render(request, 'activos/delete.html', {'form': form})


@login_required(login_url='login')
def view_activo(request, id_activo):
	activo = Activo.objects.get(id=id_activo)
	return render(request, 'activos/view.html', {'activo': activo})

@login_required(login_url='login')
def Activo_view(request):

    activo_form = ActivoForm()
    return render(request, "activos/activos.html", {"activo_form": activo_form})

def inicio(request):
    return render(request, "otros/inicio.html")

def about(request):
    return render(request, "otros/about.html")

def profile_view(request):
    user_id = request.GET.get("profile")

    try:
        profile = Profile.objects.get(id=user_id)
    except Profile.DoesNotExist:
        profile = request.user.profile

    return render(request, "otros/profile.html",
				  {"profile": profile})

def login_page(request):
	message = None

	if not request.user.is_anonymous(): # Si el usuario no tiene una sesion activa
		return redirect('inicio')

	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username = username, password = password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('base.index.html')
				else:
					message = "Tu usuario todavia no esta activos"
			else:
				message = "Nombre de usuario o password incorrecto"
	else:
		form = LoginForm()
	return render(request, "base/login.html", {'message': message, 'form': form})

@login_required(login_url = 'login')
def logout_page(request):
	logout(request)
	return redirect('inicio')

def create(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        user_form = UserForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            profile = profile_form.save(commit=False)
            profile.user_id = user.id
            profile.save()

            return HttpResponse("Formulario guardado con exito")
    else:
        profile_form = ProfileForm()
        user_form = UserForm()


    return render(request, "otros/create.html",
				  {"profile_form": profile_form,
                   "user_form": user_form})

def index(request):
	return render(request, 'base/index.html')



try:
    import StringIO
    StringIO = StringIO.StringIO
except Exception:
	from io import StringIO

def render_to_pdf(html, context_dict=None):
	"""
	template = get_template(template_src)
	context = Context(context_dict)
	html = template.render(context)
	"""
	result = StringIO()

	pdf = pisa.pisaDocument(StringIO( html ), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return HttpResponse('<pre>We had some errors</pre>')

def ReporteCargosExcelNuevo(request):
	format = request.GET.get("format", "xlsx")
	#dataSet = CargoResource().export()

	if format == "xlsx":
		nombre_archivo = "ReporteCargosExcel.xlsx"
		# Definimos que el tipo de respuesta a devolver es un archivo de microsoft excel
		#response = HttpResponse(dataSet.xlsx, content_type="application/ms-excel")
		contenido = "attachment; filename={0}".format(nombre_archivo)
		#response["Content-Disposition"] = contenido
		#return response

# Nuestra clase hereda de la vista genérica TemplateView
class ReporteCargosExcel(TemplateView):
	# Usamos el método get para generar el archivo excel
	def get(self, request, *args, **kwargs):
		# Obtenemos todas los cargos de nuestra base de datos
		"""
		cargos = Cargo.objects.all()
		if request.method == 'POST':
			form.delete()
			return redirect('cargo:index_cargo')
		# Creamos el libro de trabajo
		wb = Workbook()
		# Definimos como nuestra hoja de trabajo, la hoja activa, por defecto la primera del libro
		ws = wb.active
		# En la celda B1 ponemos el texto 'REPORTE DE CARGOS'
		ws['B1'] = 'REPORTE DE CARGOS'
		# Juntamos las celdas desde la B1 hasta la E1, formando una sola celda
		ws.merge_cells('B1:E1')
		# Creamos los encabezados desde la celda B3 hasta la E3
		ws['B3'] = 'DNI'
		ws['C3'] = 'NOMBRE_CARGO'
		ws['D3'] = 'JEFE_AREA'
		ws['E3'] = 'DESCRIPCION'
		cont = 4
		# Recorremos el conjunto de cargos y vamos escribiendo cada uno de los datos en las celdas
		for Cargo in cargos:
			ws.cell(row=cont, column=2).value = cargos.id
			ws.cell(row=cont, column=3).value = cargos.nombre_cargo
			ws.cell(row=cont, column=4).value = cargos.jefe_area
			ws.cell(row=cont, column=5).value = cargos.descripcion
			cont = cont + 1
		# Establecemos el nombre del archivo
		nombre_archivo = "ReporteCargosExcel.xlsx"
		# Definimos que el tipo de respuesta a devolver es un archivo de microsoft excel
		response = HttpResponse(content_type="application/ms-excel")
		contenido = "attachment; filename={0}".format(nombre_archivo)
		response["Content-Disposition"] = contenido
		wb.save(response)
		return response
"""
#reportes pdf
class ReporteCargosPDF(View):
	def cabecera(self,pdf):
    	#Utilizamos el archivo logo_django.png que está guardado en la carpeta static/images
		archivo_imagen = settings.STATICFILES_DIRS +'/images/inventfip.png'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
		pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)
		# Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
		pdf.setFont("Helvetica", 16)
		# Dibujamos una cadena en la ubicación X,Y especificada
		pdf.drawString(230, 790, u"INVENTFIP")
		pdf.setFont("Helvetica", 14)
		pdf.drawString(200, 770, u"REPORTE DE CARGOS")

	def get(self, request, *args, **kwargs):
		# Indicamos el tipo de contenido a devolver, en este caso un pdf
		response = HttpResponse(content_type='application/pdf')
		# La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
		buffer = BytesIO()
		# Canvas nos permite hacer el reporte con coordenadas X y Y
		pdf = canvas.Canvas(buffer)
		# Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
		self.cabecera(pdf)
		# Con show page hacemos un corte de página para pasar a la siguiente
		pdf.showPage()
		# guarda pdf
		pdf.save()
		# obtiene the value of BytestIO buffer and write response
		pdf = buffer.getvalue()
		buffer.close()
		response.write(pdf)
		return response

	def Cargo(self, pdf, y):
		# Creamos una tupla de encabezados para neustra tabla
		encabezados = ('DNI', 'NOMBRE_CARGO', 'JEFE_AREA', 'DESCRIPCION')
		# Creamos una lista de tuplas que van a contener a las personas
		detalles = [(cargo.id, cargo.nombre_cargo, cargo.jefe_area, cargo.descripcion)
					for cargo in
					Cargo.objects.all()]
		# Establecemos el tamaño de cada una de las columnas de la tabla
		detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 5 * cm, 5 * cm, 5 * cm])
		# Aplicamos estilos a las celdas de la tabla
		detalle_orden.setStyle(TableStyle(
			[
				# La primera fila(encabezados) va a estar centrada
				('ALIGN', (0, 0), (3, 0), 'CENTER'),
				# Los bordes de todas las celdas serán de color negro y con un grosor de 1
				('GRID', (0, 0), (-1, -1), 1, colors.black),
				# El tamaño de las letras de cada una de las celdas será de 10
				('FONTSIZE', (0, 0), (-1, -1), 10),
			]
		))
		# Establecemos el tamaño de la hoja que ocupará la tabla
		detalle_orden.wrapOn(pdf, 800, 600)
		# Definimos la coordenada donde se dibujará la tabla
		detalle_orden.drawOn(pdf, 60, y)

	def get(self, request, *args, **kwargs):
			# Indicamos el tipo de contenido a devolver, en este caso un pdf
			response = HttpResponse(content_type='application/pdf')
			# La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
			buffer = BytesIO()
			# Canvas nos permite hacer el reporte con coordenadas X y Y
			pdf = canvas.Canvas(buffer)
			# Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
			self.cabecera(pdf)
			y = 600
			self.tabla(pdf, y)
			# Con show page hacemos un corte de página para pasar a la siguiente
			pdf.showPage()
			pdf.save()
			pdf = buffer.getvalue()
			buffer.close()
			response.write(pdf)
			return response