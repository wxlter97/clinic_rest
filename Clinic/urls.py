from django.urls import path, re_path
from . import views

urlpatterns = [
    path('rol/', views.rolList.as_view()),
    re_path(r'^rol/(?P<pk>[0-9]+)/$', views.rolDetail.as_view()),

    path('usuario/', views.usuarioList.as_view()),
    re_path(r'^usuario/(?P<pk>[0-9]+)/$', views.usuarioDetail.as_view()),

    path('paciente/', views.pacienteList.as_view()),
    re_path(r'^paciente/(?P<pk>[0-9]+)/$', views.pacienteDetail.as_view()),

    path('especialidad/', views.especialidadList.as_view()),
    re_path(r'^especialidad/(?P<pk>[0-9]+)/$', views.especialidadDetail.as_view()),

    path('medico/', views.medicoList.as_view()),
    re_path(r'^medico/(?P<pk>[0-9]+)/$', views.medicoList.as_view()),

    path('clinica/', views.clinicaList.as_view()),
    re_path(r'^clinica/(?P<pk>[0-9]+)/$', views.clinicaDetail.as_view()),

    path('horario/', views.horarioList.as_view()),
    re_path(r'^horario/(?P<pk>[0-9]+)/$', views.horarioDetail.as_view()),

    path('schedule/', views.scheduleList.as_view()),
    re_path(r'^schedule/(?P<pk>[0-9]+)/$', views.scheduleDetail.as_view()),

    path('medicamento/', views.medicamentoList.as_view()),
    re_path(r'^medicamento/(?P<pk>[0-9]+)/$', views.medicamentoDetail.as_view()),

    path('tipoProducto/', views.tipoProductoList.as_view()),
    re_path(r'^tipoProducto/(?P<pk>[0-9]+)/$', views.tipoProductoDetail.as_view()),

    path('producto/', views.productoList.as_view()),
    re_path(r'^producto/(?P<pk>[0-9]+)/$', views.productoDetail.as_view()),

    path('tipoEnfermedad/', views.tipoEnfermedadList.as_view()),
    re_path(r'^tipoEnfermedad/(?P<pk>[0-9]+)/$', views.tipoEnfermedadDetail.as_view()),

    path('enfermedad/', views.enfermedadList.as_view()),
    re_path(r'^enfermedad/(?P<pk>[0-9]+)/$', views.enfermedadDetail.as_view()),

    path('estadoCita/', views.estadoCitaList.as_view()),
    re_path(r'^estadoCita/(?P<pk>[0-9]+)/$', views.estadoCitaDetail.as_view()),

    path('cita/', views.citaList.as_view()),
    re_path(r'^cita/(?P<pk>[0-9]+)/$', views.citaDetail.as_view()),

    path('consulta/', views.consultaList.as_view()),
    re_path(r'^consulta/(?P<pk>[0-9]+)/$', views.consultaDetail.as_view()),

    path('receta/', views.recetaList.as_view()),
    re_path(r'^receta/(?P<pk>[0-9]+)/$', views.recetaDetail.as_view()),

    path('diagnostico/', views.diagnosticoList.as_view()),
    re_path(r'^diagnostico/(?P<pk>[0-9]+)/$', views.diagnosticoDetail.as_view()),

]