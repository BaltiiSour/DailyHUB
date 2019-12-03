from django.shortcuts import render
from .forms import ContactoForm
from django.contrib import messages

def home(request):
    return render(request,"index.html")

def galeria(request):
    return render(request,"galeria.html")

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos guardados correctamente.')
            toRender = render(request,"contacto.html")
        else:
            toRender = render(request,"contacto.html", {'ContactoForm': form})
    else:
        form = ContactoForm()
        toRender = render(request,"contacto.html", {'ContactoForm': form })
    
    return toRender