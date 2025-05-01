from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from apps.usuarios.models import Usuario

def login_view(request):
    if request.method == 'POST':
        nombre_usuario = request.POST.get('username')
        contrasena = request.POST.get('password')
        rol = request.POST.get('user-type')

        try:
            usuario = Usuario.objects.get(nombre_usuario=nombre_usuario)
            
            if usuario.activo and check_password(contrasena, usuario.contrasena):
                if usuario.rol == rol:
                    request.session['id_usuario'] = usuario.id
                    request.session['nombre_usuario'] = usuario.nombre_usuario
                    request.session['rol'] = usuario.rol

                    if rol == 'directivo':
                        return redirect('dashboard_directivo')
                    else:
                        return redirect('inicio')
                else:
                    messages.error(request, 'Rol incorrecto. Seleccione el rol correcto.')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'usuarios/login.html')

def logout_view(request):
    request.session.flush()
    return redirect('inicio')

def dashboard_directivo(request):
    if request.session.get('rol') != 'directivo':
        return redirect('login')
    
    nombre = request.session.get('nombre_usuario', 'Directivo')
    return render(request, 'directivos/dashboard_directivo.html', {'nombre': nombre})
