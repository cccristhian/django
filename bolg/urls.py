from django.conf.urls import include, url
from . import views

urlpatterns = [
#cuando la linea este vasia nos envia a la siguiente vista
        url(r'^$', views.listar_publicacion),
]
