from .forms import postearForm
from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Publicar


def listar_publicacion(request):
    publi = Publicar.objects.filter(fecha_publica__lte=timezone.now()).order_by('fecha_publica')
     #se busca en la carpeta de template el blog
    return render(request, 'blog/listar_publicacion.html', {'publi':publi})
def detalle_pub(request,pk):
    p=get_object_or_404(Publicar, pk=pk)
    return render(request,'blog/detalle_pub.html', {'p':p})
def post_draft_list(request):
    publi = Publicar.objects.filter(fecha_publica__isnull=True).order_by('fecha_crear')
    return render(request, 'blog/post_draft_list.html', {'publi': publi})

def post_remove(request, pk):
    p = get_object_or_404(Publicar, pk=pk)
    p.delete()
    return redirect('/')

def post_publish(request, pk):
    p = get_object_or_404(Publicar, pk=pk)
    p.publish()
    return render(request,'blog/detalle_pub.html', {'p':p})

def nueva_publicacion(request):
    if request.method == "POST":#verifica que sea la primera vez que se ingresa al sistema
        f = postearForm(request.POST)
        if f.is_valid():#//si ya gue llamado una vez se recuperan los datos ingresados anteriormente
            p = f.save(commit=False)#//abre la conexion
            p.autor = request.user#//usuario que esta logueado
            #p.fecha_publica = timezone.now()
            p.save()#//guardar en la base de datos
            return redirect('postear', pk=p.pk)
    else:
        f = postearForm()
        return render(request, 'blog/nueva_publicacion.html', {'f': f})
