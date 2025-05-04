from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-szt(26&cmzc011qr-0raq!0tm0#d-n&sp31urxs3^_hdyc+t(6'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',  
    'apps.usuarios',
    'apps.estudiantes',
    'apps.tutores',
    'apps.docentes',
    'apps.secretarias',
    'apps.directivos',
    'apps.asignaturas',
    'apps.inscripciones',
    'apps.notas',
    'apps.asistencia',
    'apps.vark',
    'apps.publico',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'apps' / 'publico' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'



""""
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
"""

#BASE DE DATOS DE AILYN
"""
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'englishclub',
        'HOST': 'DESKTOP-RI7UI8N\\SQLEXPRESS',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'trusted_connection': 'yes',
        },
    }
}
"""

#BASE DE DATOS MARIOLY

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'englishclub',
        'HOST': 'LAPTOP-M4R1\\SQLEXPRESS',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'trusted_connection': 'yes',
        },
    }
}


#BASE DE DATOS DE LIMBER
"""
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'englishclub',
        'HOST': 'LINO\\SQLEXPRESS',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'trusted_connection': 'yes',
        },
    }
}
"""

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'es-bo'

TIME_ZONE = 'America/La_Paz'

USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

# es para manejar archivos estaticos como esta en la raiz static importante no borrar
STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
