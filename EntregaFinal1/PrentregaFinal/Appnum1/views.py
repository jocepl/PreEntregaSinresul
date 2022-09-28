from django.shortcuts import render
from django.http import HttpResponse
from Appnum1.forms import *
from Appnum1.models import *

# Create your views here.

def inicio(request):
    return render(request, "Appnum1/inicio.html")

def trabajadores(request):
    return render(request, "Appnum1/colab.html")

def comprador(request):
    return render(request, "Appnum1/buyer.html")

def vendedores(request):
    return render(request, "Appnum1/seller.html")

def colabformulario(request):
    if request.method == "POST":
        formulario1 = ColabFormulario(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            colaborador = colabs(colab_legajo = info["legajo"],
                                colab_nombre = info["nombre"], 
                                colab_apellido = info["apellido"], 
                                colab_edad = info["edad"],
                                colab_categoria_venta= info["categoria_venta"])
            colaborador.save()
            return render(request, "Appnum1/inicio.html")
    else:
        formulario1 = ColabFormulario()
    return render(request, "Appnum1/formu_colab.html", {"form1":formulario1})

def buyerformulario(request):
    if request.method == "POST":
        formulario2 = BuyerFormulario(request.POST)
        if formulario2.is_valid():
            info2 = formulario2.cleaned_data
            comprador = buyers(b_nombre = info2["nombre"], b_apellido = info2["apellido"], b_email= info2["email"], b_direccion=info2["direccion"], b_tlf = info2["tlf"])
            comprador.save()
            return render(request, "Appnum1/inicio.html")
    else:
        formulario2 = BuyerFormulario()
    return render(request, "Appnum1/formu_buyer.html", {"form2":formulario2})


def sellerformulario(request):
    if request.method == "POST":
        formulario3 = SellerFormulario(request.POST)
        if formulario3.is_valid():
            info3 = formulario3.cleaned_data
            vendedor = sellers(seller_nombre = info3["nombre"],seller_categoria= info3["categoria"], seller_email=info3["email"])
            vendedor.save()
            return render(request, "Appnum1/inicio.html")
    else:
        formulario3 = SellerFormulario()
    return render(request, "Appnum1/formu_seller.html", {"form3":formulario3})


def busquedalejago(request):
    return render(request, "Appnum1/inicio.html")


def resultados(request):

    if request.GET["legajo"]:

        legajo = request.GET["legajo"]
        colab = colabs.objects.filter(colab_legajo__iexact = legajo)

        return render(request, "Appnum1/resultados.html", {"legajo":legajo, "nombre":colab})
    else:
        respuesta = "Debes colocar el legajo del trabajador."
    
    return HttpResponse(respuesta)