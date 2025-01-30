import environ
import os
from pathlib import Path
from datetime import timedelta
from cryptography.fernet import Fernet

env = environ.Env()


BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&n3lx^&ynw!jf4xu_9in&ct6cn-!ig7+qsrkj@wx-zjsx^(^%d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# DEBUG = env("DEBUG")
# SQL = env("SQL")
# SERVER = env("SERVER")

# if SERVER == "on":
#     ALLOWED_HOSTS = ["", ".onrender.com", "*"]
# else:
#     ALLOWED_HOSTS = ["*"]

# ALLOWED_HOSTS = []


# Application definition
# pip install django-registration

INSTALLED_APPS = [
    "corsheaders",
    "dal",
    "dal_select2",
    "drf_yasg",
    "el_pagination",
    "rest_framework",
    "rest_framework_simplejwt",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "customer",
    "services",
    "main",
    "main_admin",
    "users",
    "reports",
    'financials',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'finance.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'finance.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# if SERVER == "on":
#     DATABASES = {
#         "default": dj_database_url.config(
#             default=os.environ.get("DATABASE_URL"),
#             conn_max_age=600,
#             conn_health_checks=True,
#         )
#     }
# else:
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.postgresql_psycopg2",
#             "NAME": env("DB_NAME"),
#             "USER": env("DB_USER"),
#             "PASSWORD": env("DB_PASSWORD"),
#             "HOST": env("DB_HOST"),
#             "PORT": env("DB_PORT"),
#         }
#     }

# AUTH_USER_MODEL ="main_admin.CustomUser"

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Customization of the lifetime of the access and refresh tokens

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=210),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=730),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ]
}

# from rest_framework.permissions import AllowAny, IsAuthenticated

CORS_ALLOW_ALL_ORIGINS = True


CORS_ALLOW_HEADERS = [
    "content-type",
    "authorization",
    "x-requested-with",
    "accept",
    "origin",
    "user-agent",
    "cache-control",
    "x-csrftoken",
    "accept-encoding",
    "content-disposition",
]


CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]


CORS_ALLOW_CREDENTIALS = True


CORS_ALLOWED_ORIGINS = [
    "http://localhost:5000",
]


PASSWORD_ENCRYPTION_KEY = os.environ.get(
    "PASSWORD_ENCRYPTION_KEY", Fernet.generate_key()
)

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000", 
    "https://your-frontend.com",
]
