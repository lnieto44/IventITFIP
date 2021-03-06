from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from inventario.views import login_page, logout_page, profile_view, create, Activo_view, inicio, about, index_cargo, \
    view_cargo, \
    create_cargo, delete_cargo, edit_cargo, index, ReporteCargosExcel, ReporteCargosPDF, ReporteCargosExcelNuevo, \
    create_activo,index_activo,edit_activo,delete_activo,view_activo, logout

urlpatterns = [
    url(r'^login/', login_page, name='login'),
    url(r'^profile$', profile_view, name='profile'),
    url(r'^create$', create, name='create'),
    url(r'^activos$', index_activo, name='index_activo'),
    url(r'^activos/create/', create_activo, name='create_activo'),
    url(r'^activos/edit/(?P<id_activo>\d+)/$', edit_activo, name='edit_activo'),
    url(r'^activos/delete/(?P<id_activo>\d+)/$', delete_activo, name='delete_activo'),
    url(r'^activos/view/(?P<id_activo>\d+)/$', view_activo, name='view_activo'),
    url(r'^inicio$', inicio, name='inicio'),
    url(r'^index/', index, name='index'),
    url(r'^$', inicio, name='inicio'),
    url(r'^about$', about, name='about'),
    url(r'^cargos$', index_cargo, name='index_cargo'),
    url(r'^cargos/new/', create_cargo, name='create_cargo'),
    url(r'^cargos/edit/(?P<id_cargo>\d+)/$', edit_cargo, name='edit_cargo'),
    url(r'^cargos/delete/(?P<id_cargo>\d+)/$', delete_cargo, name='delete_cargo'),
    url(r'^cargos/view/(?P<id_cargo>\d+)/$', view_cargo, name='view_cargo'),
    url(r'^reporte_cargos_pdf/$', login_required(ReporteCargosPDF.as_view()), name="reporte_cargos_pdf"),
    url(r'^reporte_cargos_excel/$', ReporteCargosExcel.as_view(), name="reporte_cargo_excel"),
    url(r'^salir$', logout, name="salir", kwargs={'next_page': '/'}),

]