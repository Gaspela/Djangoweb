from django.shortcuts import redirect, render
from .models import User
from .forms import UserForm
# Representa la vista del template, Logica del proyecto
# Create your views here.


def init(request):
    personas = User.objects.all()
    contexto = {
        'user': personas
    }
    return render(request, 'index.html', contexto)


def createUser(request):
    if request.method == "GET":
        form = UserForm()
        contexto = {
            'form': form
        }
    else:
        form = UserForm(request.POST)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'create_user.html', contexto)


def editUser(request, id):
    personas = User.objects.get(id=id)
    if request.method == "GET":
        form = UserForm(instance=personas)
        contexto = {
            'form': form
        }
    else:
        form = UserForm(request.POST, instance=personas)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'create_user.html', contexto)

def delteUser(request, id):
    personas = User.objects.get(id=id)
    personas.delete()
    return redirect('index')
    
    
