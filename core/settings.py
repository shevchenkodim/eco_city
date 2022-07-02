from pathlib import Path
import environ
from django.core.management.utils import get_random_secret_key

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()

DEBUG = env.bool('DEBUG', default=False)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env.str('SECRET_KEY', get_random_secret_key())

ALLOWED_HOSTS = ["*"]

CORS_ALLOW_ALL_ORIGINS = env.bool('CORS_ALLOW_ALL_ORIGINS', False)
CORS_ALLOWED_ORIGINS = [
    env.str('ALLOWED_ORIGIN_WEB', 'http://127.0.0.1:8000')
]
CSRF_TRUSTED_ORIGINS = [
    env.str('TRUSTED_ORIGIN_WEB', 'http://127.0.0.1:8000')
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',

    'common',
    'broker'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'core.wsgi.application'

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env.str('DB_NAME'),
            'USER': env.str('DB_USER'),
            'PASSWORD': env.str('DB_PASSWORD'),
            'HOST': env.str('DB_HOST'),
            'PORT': env.str('DB_PORT'),
        }
    }

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

# redis
REDIS_DB = env.int('REDIS_DB', '0')
REDIS_HOST = env.str('REDIS_HOST', 'localhost')
REDIS_PORT = env.str('REDIS_PORT', '6379')
REDIS_USER = env.str('REDIS_USER', '')
REDIS_PROTOCOL = env.str('REDIS_PROTOCOL', 'redis')
REDIS_PASSWORD = env.str('REDIS_PASSWORD', '')
REDIS_CONNECTION_URL = f"{REDIS_PROTOCOL}://{REDIS_USER}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

# celery
CELERY_BROKER_URL = env.str('REDIS_CONNECTION_URL', REDIS_CONNECTION_URL)
CELERY_BROKER_TRANSPORT = env.str('CELERY_BROKER_TRANSPORT', 'redis')

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = []

MEDIA_URL = '/mediafiles/'

MEDIA_ROOT = BASE_DIR / 'mediafiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

FIXTURE_DIRS = ("fixtures",)

ECO_KMDA_URL_SENSOR_DATA = "https://asm.kyivcity.gov.ua//data/get-data"
ECO_KMDA_URL_SENSORS_INFO = "https://asm.kyivcity.gov.ua//data/json-sensors-by-device-id"
