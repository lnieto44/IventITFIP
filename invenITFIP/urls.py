from django.conf.urls import url, include
from django.contrib import admin




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('inventario.urls')),
    url(r'^', include('inventario.urls', namespace='cargo')),
    url(r'^', include('inventario.urls', namespace='activo')),

]

