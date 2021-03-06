from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from .models import Pelicula, Cliente, Funcion
from .forms import RegistroCliente
from django.urls import reverse_lazy

# Create your views here.
class Home(TemplateView):
    template_name = 'cine/index.html'
    
class RegistroCliente(CreateView):
    model = Cliente
    form_class = RegistroCliente
    template_name = 'cine/cliente/registro_cliente.html'
    success_url = reverse_lazy('cine:list.pelicula')

class UpdateCliente(UpdateView):
    model = Cliente
    form_class = RegistroCliente
    template_name = 'cine/cliente/update_cliente.html'
    success_url = reverse_lazy('cine:list.cliente')
    
class ListFuncion(ListView):
    model = Funcion
    template_name = 'cine/pelicula/list_funcion.html'
    queryset = Funcion.objects.all()
    context_object_name = 'funciones'

class ListPeliculas(ListView):
    model = Pelicula
    template_name = 'cine/pelicula/list_pelicula.html'
    queryset = Pelicula.objects.all()
    context_object_name = 'peliculas'