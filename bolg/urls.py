from django.conf.urls import include, url
from . import views

urlpatterns = [
#cuando la linea este vasia nos envia a la siguiente vista
        url(r'^$', views.listar_publicacion),
        url(r'^postear/(?P<pk>[0-9]+)/$', views.detalle_pub, name='postear'),
        url(r'^postear/nuevo/$', views.nueva_publicacion, name='nueva_publicacion'),
]
