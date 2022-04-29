from django.shortcuts import render, redirect
from agenda_contactos.models import AgendaContacto  
from agenda_contactos.forms import AgendaContactoForm  

# Create your views here.
def agenda(request):  
    if request.method == "POST":  
        form = AgendaContactoForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/mostrar-contactos')  
            except:  
                pass  
    else:  
        form = AgendaContactoForm()  
    return render(request,'index.html',{'form':form})  
def mostrarContactos(request):  
    contactos = AgendaContacto.objects.all()  
    return render(request,"mostrar_contactos.html",{'contactos':contactos})  
def editarContacto(request, id):  
    contacto = AgendaContacto.objects.get(id=id)  
    return render(request,'editar_contacto.html', {'contacto':contacto})  
def actualizarContacto(request, id):  
    contacto = AgendaContacto.objects.get(id=id)  
    form = AgendaContactoForm(request.POST, instance = contacto)  
    if form.is_valid():  
        form.save()  
        return redirect("/mostrar-contactos")  
    return render(request, 'editar-contacto.html', {'contacto': contacto})  
def eliminarContacto(request, id):  
    contacto = AgendaContacto.objects.get(id=id)  
    contacto.delete()  
    return redirect("/mostrar-contactos") 
