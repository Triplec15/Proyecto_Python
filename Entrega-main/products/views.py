from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse

from products.models import Products
from products.forms import Product_form
from products.forms import Contacto_form
from products.forms import Categoria_form

# Create your views here.
def products(request):
    if not request.user:
        return redirect('/accounts/iniciar')

    
    productos = Products.objects.all()
    context = {'productos':productos}
    return render(request, 'products.html', context=context)

def categoria(request):
    data_cat ={ 
        'form': Categoria_form() 
    }
    return render(request, 'categoria.html', data_cat)

def contacto(request):
    data ={ 
        'form': Contacto_form() 
    }
    
    if request.method =='POST':
        formulario = Contacto_form(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto enviado"
        else:
            data["form"] = formulario 
    
    return render(request, 'contacto.html', data)

def create_product_view(request):
    if request.method == 'GET':
        form = Product_form()
        context = {'form':form}
        return render(request, 'create_product.html', context=context)
    else:
        form = Product_form(request.POST)
        if form.is_valid():
            new_product = Products.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                SKU = form.cleaned_data['SKU'],
                active = form.cleaned_data['active'],
            )
            context ={'new_product':new_product}
        return render(request, 'create_product.html', context=context)

def search_product_view(request):
    print(request.GET)
    products = Products.objects.filter(name__contains = request.GET['search'])
    context = {'products':products}
    return render(request, 'search_product.html', context = context)
