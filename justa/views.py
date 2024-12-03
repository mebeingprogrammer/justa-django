from django.shortcuts import render
from .models import Usuarios
from .models import posts

def index(request):
    return render(request, 'index.html', {})

def login_modal(request):
    return render(request, 'modals/login.html', {})

def register_modal(request):
    return render(request, 'modals/register.html', {})

def blogs(request):
    return render(request, 'blogs.html', {})

def politicas(request):
    return render(request, 'politicas.html', {})

def mainpage(request):
    posts_list = posts.objects.all()
    return render(request, 'mainpage.html', {'posts': posts_list})

def register(request):
    x=request.POST['name']
    y=request.POST['email']
    z=request.POST['password']
    mem=Usuarios(Nombre=x, email=y, password=z)
    mem.save()
    return render(request, 'mainpage.html', {})

def login(request):
    if request.method == 'POST':
        y = request.POST.get('emaillog', '')
        z = request.POST.get('passwordlog', '')

        # Filtrar si el email y el password coinciden con un usuario existente
        if Usuarios.objects.filter(email=y, password=z).exists():
            # Si las credenciales son correctas, redirigir al index
            return render(request, 'mainpage.html', {})
        else:
            # Si las credenciales son incorrectas, regresar a la página de login con un mensaje de error
            return render(request, '/', {'error': 'Credenciales incorrectas'})
