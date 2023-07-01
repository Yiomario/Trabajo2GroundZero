from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormularioForm, ProductoForm, Producto,CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def formulario(request):
    data = { 
        'form': FormularioForm()
    }

    if request.method == 'POST':  
        formulario = FormularioForm(data=request.POST)
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

@permission_required('app.add_producto')
def agregar_producto(request):


    data ={
        'form': ProductoForm()
    }
    if request.method == 'POST':
        stock = ProductoForm (data=request.POST, files=request.FILES)
        if stock.is_valid():
            stock.save()
            messages.success(request, "Se agregó correctamente") 
        else:
            data["form"] = stock

    return render(request, 'app/producto/agregar.html',data)  
@permission_required('app.view_producto')
def listar_productos(request):
    productos = Producto.objects.all()

    data = {
        'productos':productos
    }
    return render(request, 'app/producto/listar.html', data)
@permission_required('app.change_producto')
def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)  
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        stock = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if stock.is_valid():
            stock.save()
            messages.success(request, "modificado correctamente")
            return redirect(to=listar_productos)
        data['form'] = stock

    return render(request, 'app/producto/modificar.html', data)  
@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)  
    producto.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listar_productos")  

def registro(request):
    data = {
        'form' : CustomUserCreationForm()

    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "te has registrado correctamente")
            return redirect(to="index")
        data['form'] = formulario
    return render(request, 'registration/registro.html', data)
