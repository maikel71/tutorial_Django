from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

from django.views.generic import *
# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/lista_proveedor/')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username, password=password)
                if usuario is not None and usuario.is_active:
                    login(request, usuario)
                    return HttpResponseRedirect('/lista_proveedor/')
        else:
            form = LoginForm()
            ctx = {'form': form}
            return render(request, 'login.html', ctx)


@login_required(login_url='/login')
def inicio_view(request):
    productos = Producto.objects.all()
    ctx = {'productos': productos}
    return render(request, 'index.html', ctx)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')


#================ VISTAS BASADAS EN CLASES=============#
class ListadoProveedor(ListView):
    model = Proveedor
    template_name = 'plantilla/listar_proveedor.html'
    queryset = Proveedor.objects.filter(estado=True)
    context_object_name = 'proveedores'


class CrearProveedor(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'plantilla/crear_proveedor.html'
    success_url = reverse_lazy('lista_proveedor')
