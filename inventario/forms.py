from django import forms
from django.contrib.auth.models import User
from .models import Activo, Tipo_material, TipoActivo, Inventario, Municipio, Sede, Programa, Profile,\
    Dependencia, IngresoActivo, Cargo, Entrada_Articulos, DetalleIngresoActivo,Ubicacion, Categoria, Proveedor, \
    Detalle_entrada_articulos, Facultad

class ActivoForm(forms.ModelForm):

	class Meta:
		model = Activo

		fields = [
			'nombre_activo',
			'precio_activo',
			'estado_activo',
			'existencias',
			'fecha',
			't_material',
			'tipo_activo',
			'inventario',
		]
		labels = {
			'nombre_activo': 'Nombres',
			'precio_activo': 'Apellidos',
			'estado_activo': 'Celular',
			'existencias':'Fecha',
			'fecha': 'Producto',
			't_material':'Tipo_material',
			'tipo_activo':'Tipo_activo',
			'inventario':'Inventario',

		}
		widgets = {
			'nombre_activo': forms.TextInput(attrs={'class':'form-control'}),
			'precio_activo': forms.TextInput(attrs={'class':'form-control'}),
			'estado_activo': forms.TextInput(attrs={'class':'form-control'}),
			'existencias': forms.TextInput(attrs={'class':'form-control'}),
			'fecha': forms.Select(attrs={'class':'form-control'}),
			't_material': forms.TextInput(attrs={'class': 'form-control'}),
			'tipo_activo': forms.TextInput(attrs={'class': 'form-control'}),
			'inventario': forms.Select(attrs={'class': 'form-control'}),

		}


class Tipo_materialForm(forms.ModelForm):
    class Meta:
        model = Tipo_material
        fields = "__all__"
        labels = {
            "clase_material": "Tipo de material",
        }
        widgets = {
            "clase_material": forms.TextInput(attrs={"class": "form-control"}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"
        labels = {
            "nombre_categoria": "Nombre De La Categoria",

        }

        widgets = {
            "nombre_categoria": forms.TextInput(attrs={"class": "validate"}),

        }

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ("descripcion_inventario",)

        labels = {
             "descripcion_inventario": "Nombre De La Categoria",

        }

        widgets = {
            "descripcion_inventario": forms.TextInput(attrs={"class": "validate"}),

        }

class TipoActivoForm(forms.ModelForm):
    class Meta:
        model = TipoActivo
        fields = ("descripcion","tipo_activo")

class ActivoForm(forms.ModelForm):
    class Meta:
        model = Activo
        fields = ("nombre_activo", "precio_activo", "estado_activo", "existencias",
                      "fecha", "t_material", "tipo_activo", "inventario",)

        labels = {
            "nombre_activo": "Nombre Activo",
            "precio_activo": "Precio Activo",
            "estado_activo": "Estado del Activo",
            "existencias": "Existencias Activo",
            "fecha": "Fecha Activo",
            "t_material": "Tipo Activo",
            "inventario": "Inventario"

        }
        widgets = {
            "nombre_activo": forms.TextInput(attrs={"class": "validate"}),
            "precio_activo": forms.NumberInput(attrs={"class": "validate"}),
            "estado_activo": forms.Select(attrs={"class": "form-control"}),
            "existencias": forms.NumberInput(attrs={"class": "validate"}),
            "fecha": forms.DateInput(attrs={"class": "validate"}),
            "t_material": forms.Select(attrs={"class": "form-control"}),
            "tipo_activo": forms.Select(attrs={"class": "form-control"}),
            "inventario": forms.Select(attrs={"class": "form-control"}),
         }

class ProfileForm(forms.ModelForm):
     class Meta:
        model = Profile
        fields = ("fecha_nacimiento", "sexo",)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email",)

class IngresoActivoForm(forms.ModelForm):
    class Meta:
        model = IngresoActivo
        fields = ("proveedor", "fecha_registro", "doc_origen",)

class DetalleIngresoActivoForm(forms.ModelForm):
    class Meta:
        model = DetalleIngresoActivo
        fields = "__all__"

class Entrada_ArticuloForm(forms.ModelForm):
    class Meta:
        model = Entrada_Articulos
        fields = "__all__"

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = "__all__"

class CargoForm(forms.ModelForm):

	class Meta:
		model = Cargo

		fields = [
			"nombre_cargo",
			"jefe_area",
			"descripcion",
		]

		labels = {
			"nombre_cargo": "Nombre",
			"jefe_cargo": "Jefe_cargo",
			"descripcion": "Descripcion",
		}

		widgets = {
			"nombre_cargo": forms.TextInput(attrs={"class": "validate"}),
			"jefe_cargo": forms.RadioSelect(attrs={"class":"form-control"}),
			"descripcion": forms.TextInput(attrs={"class": "validate"}),
		}
class LoginForm(forms.ModelForm):

	class Meta:
		model = User

		fields = [
			"username",
			"password",
		]

		labels = {
			"username": "Nombre_usuario",
			"password": "Clave",
		}
		widgets = {
			"username": forms.TextInput(attrs={"class": "validate"}),
			"password": forms.PasswordInput(attrs={"class": "validate"}),
		}


