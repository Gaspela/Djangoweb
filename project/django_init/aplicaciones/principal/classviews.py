from django.shortcuts import redirect, render
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from .models import User
from .forms import UserForm

"""
Funciones internas DAJNGO

calss View():
    dispatch: Verifica el metodo de la solicitud http
    hhtpnot_alloweb

    def get_contextdata(self):
        context = {}
        context['queryset'] = self.get_queryset()
        return context

    def get_queryset(self):
        return self.model.objects.all()
        
    def get_templates_names()
        return self.template_name
    
    def get(self, request, *args, **kwargs):
        return render(request,self.get_templates_name().self.get_get_queryset())
        
"""
class UserList(ListView):
    model = User
    template_name = 'index.html'
    
"""     def get_queryset(self):
        return self.model.objects.all() """
        
class CreateUser(CreateView):
    model = User
    form_class = UserForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('index')

class UpdateUser(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('index')
    
class DeleteUser(DeleteView):
    model = User
    template_name = 'checkdelete.html'
    success_url = reverse_lazy('index')

