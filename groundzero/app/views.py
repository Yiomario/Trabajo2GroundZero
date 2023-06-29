from django.shortcuts import render 
from .forms import formularioForm

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def formulario(request):
    data = { 
        'form': formularioForm()
    }

    if request.method == 'POST':  
        formulario = formularioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "formulario enviado"
        else:
            data["form"] = formulario
        

    return render(request, 'app/formulario.html', data)

def inicio(request):
    return render(request, 'app/inicio.html')

def imagen1(request):
    return render(request, 'app/imagen1.html')

def imagen2(request):
    return render(request, 'app/imagen2.html')

def imagen3(request):
    return render(request, 'app/imagen3.html')

def imagen4(request):
    return render(request, 'app/imagen4.html')

def imagen5(request):
    return render(request, 'app/imagen5.html')

def imagen6(request):
    return render(request, 'app/imagen6.html')

def imagen7(request):
    return render(request, 'app/imagen7.html')

def imagen8(request):
    return render(request, 'app/imagen8.html')




