from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent


# --- 2. DESPUÉS: El resto de la configuración ---
SECRET_KEY = 'django-insecure-...' # (El resto de tu código sigue aquí)

DEBUG = True

ALLOWED_HOSTS = ['*']


# EN EL ARCHIVO: shadecants/settings.py

# ... (arriba tendrás BASE_DIR, SECRET_KEY, DEBUG, etc.) ...

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tienda',  # <--- ¡ESTO ES LO IMPORTANTE!
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

ROOT_URLCONF = 'shadecants.urls'

WSGI_APPLICATION = 'shadecants.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'tienda.context_processors.importe_total_carrito',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Ahora sí funcionará porque BASE_DIR ya existe arriba
    }
}

# Archivos estáticos (CSS, JavaScript, Imágenes)
STATIC_URL = 'static/'

# Archivos Multimedia (Las fotos de tus perfumes)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Configuración por defecto para claves primarias (necesario en Django nuevo)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'