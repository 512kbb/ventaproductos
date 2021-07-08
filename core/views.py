from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required 
from .models import Producto, Marca

from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login


# Create your views here.

def index(request):
    return render(request, 'core/index.html')


def contacto(request):
    return render(request, 'core/contacto.html')


def feriados(request):
    return render(request, 'core/feriados.html')

def listado(request):
    listado_productos = Producto.objects.all() 
    

    data = { "lista" : listado_productos }

    return render(request, 'core/listado.html', data)


@login_required
@permission_required('core.delete_producto')
def eliminar(request, id):
    producto = Producto.objects.get(id = id)

    try:
       producto.delete()
       mensaje = "Producto eliminado"
       messages.success(request, mensaje)
    except:
        mensaje = "No se pudo eliminar el producto"
        messages.Error(request, mensaje)

    return redirect('listado')


@login_required
@permission_required('core.add_producto')
def registro(request):

    listado_marcas = Marca.objects.all()

    data = {
                "marcas" : listado_marcas
            }

    if request.POST:
        producto = Producto()
        producto.codigo = request.POST.get("txtCodigo")
        producto.modelo = request.POST.get("txtModelo")
        producto.precio = request.POST.get("txtPrecio")
        producto.color = request.POST.get("txtColor")
        producto.talla = request.POST.get("txtTalla")
        producto.imagen = request.FILES.get("txtImagen")

        marca = Marca()
        marca.id = request.POST.get("cboMarca")

        producto.marca = marca


        try:
            producto.save()
            mensaje = "agregado"
            messages.success(request, mensaje)

        except:
            mensaje = "no se pudo agregar"
            messages.error(request, mensaje)

    return render(request, 'core/registro.html', data)


@login_required
@permission_required('core.change_producto')
def modificar(request, id):
    producto = Producto.objects.get(id = id)

    listado_marcas = Marca.objects.all()

    data = {
        "marcas" : listado_marcas,
        "producto" : producto
    }

    if request.POST:
        producto.codigo = request.POST.get("txtCodigo")
        producto.modelo = request.POST.get("txtModelo")
        producto.precio = request.POST.get("txtPrecio")
        producto.color = request.POST.get("txtColor")
        producto.talla = request.POST.get("txtTalla")
        if request.FILES.get("txtImagen"):
            producto.imagen = request.FILES.get("txtImagen")
        

        marca = Marca()
        marca.id = request.POST.get("cboMarca")

        producto.marca = marca
    
        try:
                producto.save()
                mensaje = "modificado"
                messages.success(request, mensaje)
        except:
                mensaje = "no se pudo modificar"
                messages.error(request, mensaje)
            
        return redirect("listado")

    return render(request, "core/modificar.html", data)

def registroUsuarios(request):

    data = { "form" : CustomUserCreationForm  }

    #guardar
    if request.POST:
        formulario = CustomUserCreationForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()

            #podemos dejar logueado al usuario
            user = authenticate(username = formulario.cleaned_data["username"],
                                password = formulario.cleaned_data["password1"])

            #mensaje para swet alert
            messages.success(request, "te has registrado correctamente")

            login(request, user)
            #redirigir al index
            return redirect("index")

        data["form"] = formulario

    return render(request,  "registration/registroUsuarios.html", data)