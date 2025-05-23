from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.db import connection
from django.contrib.auth.hashers import make_password
from datetime import date
import random, string
from apps.estudiantes.forms import EstudianteFormTecnico, EstudianteFormRegular
from apps.tutores.forms import TutorForm
from apps.estudiantes.models import Estudiante
from apps.usuarios.decorators import solo_directivo
@solo_directivo
def crear_estudiante_tecnico(request):
    form = EstudianteFormTecnico(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        archivo = request.FILES.get('archivo_formulario')
        archivo_path = ''
        if archivo:
            archivo_path = f"formularios/{archivo.name}"
            with open(f"media/{archivo_path}", 'wb+') as destination:
                for chunk in archivo.chunks():
                    destination.write(chunk)
        try:
            return guardar_estudiante_y_usuario(request, data, archivo_path, origen='tecnico')
        except Exception as e:
            messages.error(request, f"❌ Error al guardar estudiante: {e}")
            return redirect('crear_estudiante_tecnico')

    return render(request, 'estudiantes/crear_estudiante_tecnico.html', {
        'form': form,
        'today': date.today()
    })
@solo_directivo
def crear_estudiante_regular(request):
    form = EstudianteFormRegular(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        fnac = data['fecha_nacimiento']
        hoy = date.today()
        edad = hoy.year - fnac.year - ((hoy.month, hoy.day) < (fnac.month, fnac.day))

        archivo = request.FILES.get('archivo_formulario')
        archivo_path = ''
        if archivo:
            archivo_path = f"formularios/{archivo.name}"
            with open(f"media/{archivo_path}", 'wb+') as destination:
                for chunk in archivo.chunks():
                    destination.write(chunk)

        if edad < 18:
            serializable_data = {
                k: (v.isoformat() if isinstance(v, date) else v)
                for k, v in data.items()
            }
            serializable_data['archivo_formulario'] = archivo_path
            request.session['pendiente_estudiante'] = serializable_data
            return redirect('crear_tutor')
        else:
            return guardar_estudiante_y_usuario(request, data, archivo_path, origen='regular')

    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
    return render(request, 'estudiantes/crear_estudiante_regular.html', {
        'form': form,
        'today': date.today(),
        'dias_semana': dias_semana
    })


@solo_directivo
def crear_tutor(request):
    form = TutorForm(request.POST or None)
    estudiante_data = request.session.get('pendiente_estudiante')

    if not estudiante_data:
        messages.error(request, "No hay datos del estudiante para registrar el tutor.")
        return redirect('crear_estudiante_regular')

    if request.method == 'POST' and form.is_valid():
        try:
            archivo_path = estudiante_data.get('archivo_formulario', '')
            estudiante_data['fecha_nacimiento'] = date.fromisoformat(estudiante_data['fecha_nacimiento'])

            id_usuario_est, id_est = guardar_estudiante_y_usuario(
                request, estudiante_data, archivo_path, origen='regular', return_ids=True
            )

            if id_est is None:
                messages.error(request, 'No se pudo registrar el estudiante.')
                return redirect('crear_estudiante_regular')

            tutor_data = form.cleaned_data
            username_tutor = f"{tutor_data['nombres'][0].lower()}{tutor_data['apellidos'].split()[0].lower()}{tutor_data['ci']}".replace(" ", "").lower()
            password_tutor = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            contrasena_tutor = make_password(password_tutor)

            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO usuario (nombre_usuario, contrasena, rol, fecha_creacion, activo)
                    OUTPUT INSERTED.id
                    VALUES (%s, %s, 'tutor', %s, 1)
                """, [username_tutor, contrasena_tutor, timezone.now()])
                id_usuario_tutor = cursor.fetchone()[0]

                cursor.execute("""
                    INSERT INTO tutor (
                        ci, nombres, apellidos, fecha_nacimiento, direccion, numero, correo,
                        ocupacion, lugar_trabajo, correo_trabajo, id_usuario
                    ) OUTPUT INSERTED.id
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, [
                    tutor_data['ci'], tutor_data['nombres'], tutor_data['apellidos'], tutor_data['fecha_nacimiento'],
                    tutor_data['direccion'], tutor_data['numero'], tutor_data['correo'],
                    tutor_data['ocupacion'], tutor_data['lugar_trabajo'], tutor_data['correo_trabajo'],
                    id_usuario_tutor
                ])
                id_tutor = cursor.fetchone()[0]

                cursor.execute("""
                    INSERT INTO tiene_tutor (id_estudiante, id_tutor, parentesco)
                    VALUES (%s, %s, %s)
                """, [id_est, id_tutor, tutor_data['parentesco']])

            request.session['creado_usuario'] = f"{estudiante_data['nombres'].split()[0][0].lower()}{estudiante_data['apellidos'].split()[0].lower()}{estudiante_data['ci']}"
            request.session['creado_password'] = request.session.get('creado_password', '')
            request.session['tutor_usuario'] = username_tutor
            request.session['tutor_password'] = password_tutor

            del request.session['pendiente_estudiante']

            return redirect('estudiante_tutor_registrado')

        except Exception as e:
            import traceback
            print(traceback.format_exc())
            messages.error(request, f"Error al guardar tutor: {e}")

    elif request.method == 'POST':
        messages.error(request, "Por favor corrige los errores del formulario.")

    return render(request, 'estudiantes/crear_usuario_tutor.html', {'form': form})


@solo_directivo
def estudiante_registrado(request):
    usuario = request.session.get('creado_usuario')
    password = request.session.get('creado_password')

    request.session.pop('creado_usuario', None)
    request.session.pop('creado_password', None)

    return render(request, 'estudiantes/estudiante_registrado.html', {
        'usuario': usuario,
        'password': password
    })


@solo_directivo
def estudiante_tutor_registrado(request):
    usuario_est = request.session.pop('creado_usuario', None)
    password_est = request.session.pop('creado_password', None)
    usuario_tutor = request.session.pop('tutor_usuario', None)
    password_tutor = request.session.pop('tutor_password', None)

    return render(request, 'estudiantes/estudiante_tutor_registrado.html', {
        'usuario_est': usuario_est,
        'password_est': password_est,
        'usuario_tutor': usuario_tutor,
        'password_tutor': password_tutor,
    })


#AQUI AGREGUE LA VISTA PARA ESTUDIANTE TECNICO 
def dashboard_estudiante(request):
    if request.session.get('rol') != 'estudiante':
        return redirect('login')

    id_usuario = request.session.get('id_usuario')
    try:
        estudiante = Estudiante.objects.get(usuario_id=id_usuario)
        nombre = f"{estudiante.nombres} {estudiante.apellidos}"
    except Estudiante.DoesNotExist:
        nombre = "Estudiante"

    return render(request, 'estudiantes/dashboard_estudiante.html', {'nombre': nombre})


def guardar_estudiante_y_usuario(request, data, archivo_path, origen, return_ids=False):
    try:
        fnac = data['fecha_nacimiento']
        nombre_usuario = f"{data['nombres'].split()[0][0].lower()}{data['apellidos'].split()[0].lower()}{data['ci']}".replace(" ", "").lower()
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        contrasena_encriptada = make_password(password)

        if request.method == 'POST':
            dias_list = request.POST.getlist("dias")
            dias_str = ', '.join(dias_list)
            hora_entrada = request.POST.get("hora_entrada", "")
            hora_salida = request.POST.get("hora_salida", "")
        else:
            dias_str = data.get('dias', '')
            hora_entrada = data.get('hora', '').split('-')[0].strip() if 'hora' in data else ''
            hora_salida = data.get('hora', '').split('-')[1].strip() if 'hora' in data and '-' in data.get('hora', '') else ''

        hora_final = f"{hora_entrada} - {hora_salida}".strip() if hora_entrada and hora_salida else data.get('hora', '')

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO usuario (nombre_usuario, contrasena, rol, fecha_creacion, activo)
                OUTPUT INSERTED.id
                VALUES (%s, %s, 'estudiante', %s, 1)
            """, [nombre_usuario, contrasena_encriptada, timezone.now()])
            id_usuario = cursor.fetchone()[0]

            cursor.execute("""
                INSERT INTO estudiante (
                    ci, nombres, apellidos, fecha_nacimiento, direccion, numero, correo,
                    colegio, grupo, dias, hora, modalidad, medio_referencia, motivo_estudio,
                    archivo_formulario, fecha_inscripcion, activo, id_usuario,
                    ocupacion, tipo_estudiante, celular_referencia, correo_referencia,
                    estudios_ingles_previos, institucion_actual, tipo_inscripcion,
                    forma_pago, fecha_pago, clases_particulares, material_entregado,
                    firmado, recibido
                )
                OUTPUT INSERTED.id
                VALUES (
                    %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, 1, %s,
                    %s, %s, %s, %s,
                    %s, %s, %s,
                    %s, %s, %s, %s,
                    %s, %s
                )
            """, [
                data['ci'], data['nombres'], data['apellidos'], fnac, data['direccion'], data['numero'], data['correo'],
                data.get('colegio', ''), data.get('grupo', ''), dias_str, hora_final, data.get('modalidad', ''),
                data.get('medio_referencia', ''), data.get('motivo_estudio', ''), archivo_path, date.today(), id_usuario,
                data.get('ocupacion', ''), data.get('tipo_estudiante', ''), data.get('celular_referencia', ''),
                data.get('correo_referencia', ''), data.get('estudios_ingles_previos', ''),
                data.get('institucion_actual', ''), data.get('tipo_inscripcion', 'anual'),
                data.get('forma_pago', ''), data.get('fecha_pago', None),
                data.get('clases_particulares', False), data.get('material_entregado', False),
                data.get('firmado', False), data.get('recibido', False)
            ])
            id_estudiante = cursor.fetchone()[0]
        request.session['creado_usuario'] = nombre_usuario
        request.session['creado_password'] = password
        if return_ids:
            return id_usuario, id_estudiante
        else:
            return redirect('estudiante_registrado')
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        messages.error(request, f"❌ Error al guardar estudiante: {e}")
        if return_ids:
            return None, None
        else:
            return redirect('crear_estudiante_tecnico' if origen == 'tecnico' else 'crear_estudiante_regular')
        
    

    
        
        