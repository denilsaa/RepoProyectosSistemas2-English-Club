# 📋 Sistema de Gestión Académica - English Club

Este es un sistema de gestión académica para el Instituto English Club, desarrollado con **Django**. Proporciona una solución completa para la administración de estudiantes, docentes, tutores, notas, asistencia y la aplicación del test VARK para identificar estilos de aprendizaje. La plataforma ofrece una experiencia fluida para estudiantes, docentes, padres de familia, secretarias y directivos.

## 👥 Equipo

 => [Nombre del miembro 1] (Programador FrontEnd y Analista de QA)  
 => [Nombre del miembro 2] (Programador BackEnd)  
 => Denilson Saavedra (Coach) [https://github.com/denilsaa]

## 🛠️ Tecnologías Utilizadas

- **Django 4.x**: Framework principal del proyecto.
- **Tailwind CSS**: Para una interfaz de usuario moderna y responsiva.
- **SQL Server**: Sistema de gestión de base de datos.
- **MongoDB Atlas**: Para la generación aleatoria de preguntas VARK.
- **Python 3.10+**

## 🚀 Funcionalidades

- **Registro inteligente**: Estudiantes menores de edad requieren tutor; mayores se registran solos.
- **Gestión de usuarios**: Creación de cuentas según rol: estudiante, docente, secretaria, tutor, directivo.
- **Paneles diferenciados**: Vista específica según el tipo de usuario.
- **Notas y asistencia**: Registro y control por asignatura, grupo y horario.
- **Test VARK personalizado**: Cada estudiante recibe una prueba aleatoria y única.
- **Carga de formularios**: Posibilidad de subir archivos escaneados (PDF u otros formatos).
- **Seguridad**: Validación de edad, contraseñas cifradas, flujos limpios y controlados.

## 🛢️ Diagrama base de datos

![Diagrama](capturas/diagrama_base.png)

## 📦 Instalación

Sigue estos pasos para poner en marcha el proyecto en tu entorno local:

### 1. Clonar el repositorio
```bash
git clone https://github.com/denilsaa/RepoProyectosSistemas2-English-Club.git
cd RepoProyectosSistemas2-English-Club
```

### 2. Crear entorno virtual e instalar dependencias
```bash
python -m venv env
env\Scripts\activate        # En Windows
pip install -r requirements.txt
```

### 3. Configuración de base de datos
Edita tu archivo `settings.py` con los siguientes parámetros (si usas SQL Server local):

```python
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'englishclub',
        'HOST': 'DENIL\\SQLEXPRESS',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'trusted_connection': 'yes',
        },
    }
}
```

### 4. Migrar la base de datos
```bash
python manage.py migrate
```

### 5. Iniciar el servidor local
```bash
python manage.py runserver
```

Ahora puedes acceder al sistema en `http://localhost:8000`.

## 📋 Uso

1. **Iniciar sesión como directivo** para tener acceso total al sistema.
2. **Crear nuevos usuarios** desde el panel: estudiantes, docentes, tutores, secretarias.
3. **Registrar notas y calificaciones por grupo**.
4. **Aplicar la prueba VARK** y consultar resultados por perfil de aprendizaje.
5. **Descargar formularios o reportes académicos** si es necesario.

## 🖼️ Capturas de Pantalla

![Login](capturas/login.png)  
![Panel Directivo](capturas/panel_directivo.png)  
*Ejemplos de vistas del sistema.*

## 🤝 Contribuciones

¡Contribuciones son bienvenidas! Si deseas colaborar, sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea una rama con tu nueva funcionalidad (`git checkout -b feature/nueva-funcionalidad`)
3. Realiza un commit de tus cambios (`git commit -m "Agrega nueva funcionalidad"`)
4. Sube la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un pull request.

## 📝 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
