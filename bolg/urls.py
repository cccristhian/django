from django.conf.urls import include, url
from . import views

urlpatterns = [
#cuando la linea este vasia nos envia a la siguiente vista
        url(r'^$', views.listar_publicacion),
        url(r'^postear/(?P<pk>[0-9]+)/$', views.detalle_pub, name='postear'),
        url(r'^postear/nuevo/$', views.nueva_publicacion, name='nueva_publicacion'),
        url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
        url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
        url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
]
