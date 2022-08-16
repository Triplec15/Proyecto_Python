from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def saludo(request, nombre):
    return HttpResponse(f'Buen día {nombre} :D')

def index(request):
    return render(request, 'index.html')

def fecha_actual(request):
    fecha = datetime.now().date()
    mensaje = f'Hoy es {fecha} !!'
    return HttpResponse(mensaje)

def probando_template(request):
    context = {
        'nombre':'Christopfer',
        'apellido':'Cardoso',
        'fecha':datetime.now(),
        'edades':[18,20,5,10,12,17,22,40]
    }
    return render(request, 'template_1.html', context = context)
