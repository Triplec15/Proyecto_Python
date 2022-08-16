from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, logout
from accounts.models import DataUsuario
from django.shortcuts import redirect
from django.contrib.auth.models import User

def profile(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/iniciar')

    return render(request, 'profile.html', obtener_data_usuario(request.user))

def iniciar(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print('adssadsd')
            return redirect('/')

        else:
            return render(request, 'registration/login.html', {
                'form' : {
                    'errors': True
                }
            })

    else:
        return render(request, 'registration/login.html')
    
def signup(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')

        return render(request, 'registration/signup.html')

    elif request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        
        user = User.objects.create_user(username, email, password)
        user.save()

        login(request, user)

        return redirect('/')

    
def cerrar(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/iniciar')

    logout(request)

    return redirect('/accounts/iniciar')

def editar_perfil(request):
    if request.method == "POST":
        actualizar_datos_usuario(request.user, request.POST)

        return redirect('/accounts/profile')

    elif request.method == "GET":
    
        return render(request, 'profile_editar.html', obtener_data_usuario(request.user))


def obtener_data_usuario(usuario):
    data_usuario = DataUsuario.objects.filter(usuario=usuario)

    if data_usuario.exists(): 
        return {
            "url_imagen" : data_usuario[0].url_imagen,
            "descripcion": data_usuario[0].descripcion
        }

    return {
        "url_imagen" : "",
        "descripcion": ""
    }

def actualizar_datos_usuario(usuario,  datos):
    data_usuario = DataUsuario.objects.filter(usuario=usuario)

    if not data_usuario.exists():
        data_usuario = DataUsuario(usuario=usuario, descripcion="", url_imagen="")     
    else:
        data_usuario = data_usuario[0]

    data_usuario.url_imagen = datos['imagen']
    data_usuario.descripcion = datos['descripcion']

    data_usuario.save()
