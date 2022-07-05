from django.shortcuts import render
from appfarm.forms import ContactForm

# Create your views here.
def inicio(request):
    return render (request, 'appfarm/home.html')

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


