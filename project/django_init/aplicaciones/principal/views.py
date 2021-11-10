from django.shortcuts import render
from .models import User
# Representa la vista del template, Logica del proyecto
# Create your views here.

def init(request):
    personas = User.objects.all()
    contexto = {
        'user': personas
    }
    return render(request,'index.html', contexto)

