from django.conf.urls import url
import restfull.apirest

urlpatterns = [
    url(r'^rest/lista_items_donaciones/$', restfull.apirest.lista_items_donaciones),
    url(r'^rest/lista_lugares/$', restfull.apirest.lista_lugares),
    url(r'^rest/registrar_donacion/$', restfull.apirest.registrar_donacion),
    #url(r'^rest/configuracion/tipos_vehiculos/nuevo/$', restfull.configuracion.agregar_tipo_vehiculo)
]