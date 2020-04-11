# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from rest_framework.views import APIView

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy


from .forms import RegistroForm
from serializers import UserSerializer

class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('inventario: activo_listar')


class UserAPI(APIView):
	serializer = UserSerializer

	def get(self, request, format=None):
		lista = User.objects.all()
		response = self.serializer(lista, many=True)

		return HttpResponse(json.dumps(response.data), content_type='application/json')

