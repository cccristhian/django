from django.shortcuts import render

def listar_publicacion(request):
     #se busca en la carpeta de template el blog
        return render(request, 'blog/listar_publicacion.html', {})
