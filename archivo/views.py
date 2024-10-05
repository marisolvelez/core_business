#render se usa para renderizar plantillas HTML. Básicamente, convierte una plantilla (como un archivo .html) en una respuesta HTTP
from django.shortcuts import render, redirect 

#Este formulario será el que usemos para permitir al usuario subir un archivo Excel desde la interfaz web
from .forms import uploadFileForm

# Create your views here.

def uploadFile (request):
    #verificando si la solicitud que se está recibiendo es de tipo POST
    if request.method == 'POST':
        form = uploadFileForm(request.POST, request.FILES)
        #verifica si el formulario es válido, si esta lleno
        if form.is_valid():
            form.save()
            return redirect('archivo_subido')
    else:
        form = uploadFileForm()
    return render(request, 'file/cargar_archivo.html', {'form': form})


# Vista para mostrar la página de éxito
def archivo_subido(request):
    return render(request, 'file/archivo_exito.html')
