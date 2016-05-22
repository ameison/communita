from django.conf import settings
import os

ALLOWED_HOSTS = ['*', 'communita.abcdroid.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'platcar_dispatch',
        'USER': 'platcar_user',
        'PASSWORD': '-23_[3qddkhe%6$*#',
        'HOST': "10.240.0.4",
        'PORT': '5432',
    }
}

REDIS_HOST = '10.240.0.4'
REDIS_PORT = "6379"
REDIS_DB_CELERY = "0"
REDIS_DB_UNIDADES = "1"
REDIS_DB_SESSION = "2"
REDIS_DB_EMIT = "3"

GCM_URL = "http://gcm-http.googleapis.com/gcm/send"
GCM_KEY_SERVER = "AIzaSyAg08fLTGRaLEMvTTNEETvYRQ93UtKNDk0"
GCM_PACKAGE_NAME = "com.platcar.conductor"

#Implementacion de colas de tarea con celery
BROKER_URL = 'redis://'+REDIS_HOST+':'+REDIS_PORT+'/'+REDIS_DB_CELERY
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_IMPORTS = ("celery_tasks", )

#redis cache sessions
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://"+REDIS_HOST+":"+REDIS_PORT+"/"+REDIS_DB_SESSION,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

RUTA_FOTOS_CONDUCTORES = '/home/proyectos/platcar-imagenes/'
IMAGE_CONTAINER = 'imagenes'
IMAGE_CONTAINER_URL = '/imagenes/'

STATICFILES_DIRS = [
    os.path.join(settings.BASE_DIR, IMAGE_CONTAINER), RUTA_FOTOS_CONDUCTORES,
]