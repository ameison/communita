from django.conf import settings
import os

IP = "localhost"
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'betamedic',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '191.168.1.2',
        'PORT': '5432',
    }
}

STATICFILES_DIRS = [
    os.path.join(settings.BASE_DIR, IMAGE_CONTAINER), RUTA_FOTOS_CONDUCTORES,
]