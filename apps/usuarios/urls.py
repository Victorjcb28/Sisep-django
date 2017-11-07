from __future__ import absolute_import #importarlo para las llaves foraneas
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import UsuarioCreate,UsuarioList,UsuarioUpdate,UsuarioDelete

app_name='usuarios'
urlpatterns = [
    url(r'^registrar/$', UsuarioCreate.as_view(), name='usuario_crear'),
    #url(r'^ureg/$', Usuariocre, name='usuario_cre'),
    url(r'^listar$', login_required(UsuarioList.as_view()), name='usuario_listar'),
    #url(r'^editar/(?P<id_user>\d+)/$',UsuarioUpdate,name='usuario_editar'),
    url(r'^editar/(?P<pk>\d+)$', login_required(UsuarioUpdate.as_view()), name='usuario_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', UsuarioDelete.as_view(), name='usuario_eliminar'),
    
   
]   
