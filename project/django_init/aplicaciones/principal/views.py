from django.shortcuts import render
from .models import User
# Representa la vista del template, Logica del proyecto
# Create your views here.

def init(request):
    return render(request,'index.html')