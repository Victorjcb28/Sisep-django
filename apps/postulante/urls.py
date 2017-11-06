
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from .views import PostulanteCreate, PostulanteList,PostulanteUpdate,PostulanteDelete,PostulanteSeleccion,PreguntasSeleccion,ExamenAdminCreate,ExamenList,CargoCreate,CargoList,CargoUpdate,CargoDelete,CargoListAll
app_name='postulante'
urlpatterns = [
    

    url(r'^seleccion/$', PostulanteSeleccion,name='postulante_seleccion'),
    url(r'^selecpreg/$', PreguntasSeleccion.as_view(),name='pregunta_seleccion'),

    url(r'^registrar/(?P<pk>\d+)$', PostulanteCreate.as_view(), name='postulante_crear'),
    
    url(r'^examenad/(?P<pk>\d+)/(?P<cargo>\d+)$', ExamenAdminCreate.as_view(), name='examen_admin'),
    
    url(r'^cargo/$', CargoCreate.as_view(), name='cargo_crear'),
   
    url(r'^examenlist/$', ExamenList, name='examen_listar'),
    url(r'^listar/$', PostulanteList.as_view(), name='postulante_listar'),
    url(r'^cargolist/$', CargoList.as_view(), name='cargo_listar'),
    url(r'^cargolistall/$', CargoListAll.as_view(), name='cargosall_listar'),
    
   	
    url(r'^editar/(?P<pk>\d+)$', PostulanteUpdate.as_view(), name='postulante_editar'),
    url(r'^cargoedit/(?P<pk>\d+)$', CargoUpdate.as_view(), name='cargo_editar'),

    url(r'^eliminar/(?P<pk>\d+)$', PostulanteDelete.as_view(), name='postulante_eliminar'),
    url(r'^cargodele/(?P<pk>\d+)$', CargoDelete.as_view(), name='cargo_eliminar'),
   	

    
]