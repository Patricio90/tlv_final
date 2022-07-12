from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from django.shortcuts import render
from appfarm.forms import ContactForm

# Create your views here.
def inicio(request):
    return render (request, 'appfarm/home.html')

def nosotros(request):
    return render(request, 'appfarm/nosotros.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/index.html', {'productos': productos})

def listar(request):
    productos = Producto.objects.all()
    return render(request, 'appfarm/lista.html', {'productos': productos})

def carro(request):
    return render(request, 'appfarm/carro.html')

def crear_producto(request):
    formulario = ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.instance.autor = request.user
        formulario.save()
        return redirect('productos')
    return render(request, 'productos/crear.html', {'formulario': formulario})   

def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.user == producto.autor:
        formulario = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
        if formulario.is_valid() and request.POST:
            formulario.save()
            return redirect('productos')
        return render(request, 'productos/editar.html', {'formulario': formulario})
    return redirect('productos')

def eliminar(request, id):
    producto = Producto.objects.get(id=id)
    if request.user == producto.autor:
        producto.delete()
        return redirect('productos')
    return redirect('productos')
def about(request):
    return render(request, 'appfarm/about.html')

def contacto(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            nombre=form.cleaned_data["nombre"]
            email=form.cleaned_data["email"]
            Telefono=form.cleaned_data["Telefono"]
            cuerpo=form.cleaned_data["cuerpo"]
            print(nombre,email,Telefono,cuerpo)
    form=ContactForm()
    return render(request,'appfarm/contacto.html',{"form":form})


